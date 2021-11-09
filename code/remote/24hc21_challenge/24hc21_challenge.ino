#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <DNSServer.h>

#include "AppConfig.h"
#include "AppHttp.h"
#include "ota_helpers.h"

AppConfig config;
ESP8266WebServer webserver(80);
AppHttp http_handler(config, webserver);
DNSServer dns;
bool connect_enabled;
bool ap_enabled;
bool apfallback_enabled;

const int leds[] = {D0, D3, D4};
int led_nb = 0;

void setup() {
  pinMode(D0, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  digitalWrite(D0, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);

  pinMode(D2, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D8, OUTPUT);
  digitalWrite(D2, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D8, HIGH);

  pinMode(D6, INPUT_PULLUP);
  pinMode(D5, INPUT_PULLUP);
  pinMode(D7, INPUT_PULLUP);

  Serial.begin(115200);
  Serial.println("Starting 24HC21 remote control");

  config.readFromEEPROM();
  if (!strcmp(config.hostname, "")) {
    char hostString[13];
    sprintf(hostString, "GHC64_%06X", ESP.getChipId());
    config.hostname.setValue(hostString);
  }

  connect_enabled = config.connect_enabled;
  ap_enabled = config.ap_enabled;
  apfallback_enabled = config.apfallback_enabled;

  Serial.print("Hostname: ");
  Serial.println(config.hostname);

  webserver.begin();
  WiFi.hostname(config.hostname);
  if (MDNS.begin(config.hostname)){
    MDNS.addService("http", "tcp", 80);
  }
  ota_setup(config.hostname);

  Serial.print("Connection to wifi");
  if (config.connect_enabled && strcmp(config.connect_essid, "")) {
    Serial.print(": \"");
    Serial.print(config.connect_essid);
    Serial.println('"');
    WiFi.begin(config.connect_essid, config.connect_password);
  } else {
    Serial.println(" disabled");
  }
  
  Serial.print("Wifi access point");
  if (config.ap_enabled && strcmp(config.ap_essid, "")) {
    Serial.print(": \"");
    Serial.print(config.ap_essid);
    Serial.print('"');
    if (WiFi.softAP(config.ap_essid, config.ap_password)) {
      Serial.print(' ');
      Serial.println(WiFi.softAPIP());
      dns.start(53, "*", WiFi.softAPIP());
    } else {
      Serial.println(" failed");
      ap_enabled = false;
    }
  } else {
    WiFi.softAPdisconnect();
    Serial.println(" disabled");
  }

  MDNS.begin(config.hostname.value());
}

bool connectionFailed = false;
int connectCounter = 0;
long next_change = 0;
void loop() {
  ota_loop();
  dns.processNextRequest();
  webserver.handleClient();

  if (WiFi.status() == WL_CONNECTED) {
    long time = millis();
    if (time > next_change) {
      next_change = time + 200;
      led_nb = (led_nb + 1) % 3;
      digitalWrite(D0, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
      digitalWrite(leds[led_nb], LOW);
    }
  }

  digitalWrite(D2, LOW);
  if (!digitalRead(D6)) Serial.println("X+");
  if (!digitalRead(D5)) Serial.println("Y+");
  if (!digitalRead(D7)) Serial.println("Z+");
  digitalWrite(D2, HIGH);

  digitalWrite(D1, LOW);
  if (!digitalRead(D6)) Serial.println("X-");
  if (!digitalRead(D5)) Serial.println("Y-");
  if (!digitalRead(D7)) Serial.println("Z-");
  digitalWrite(D1, HIGH);

  digitalWrite(D8, LOW);
  if (!digitalRead(D6)) Serial.println("✗");
  if (!digitalRead(D5)) Serial.println("•");
  if (!digitalRead(D7)) Serial.println("✓");
  digitalWrite(D8, HIGH);

  // Connection indicator
  if (connect_enabled && !connectionFailed) {
    if (WiFi.status() != WL_CONNECTED) {
      if (connectCounter == 50) {
        digitalWrite(D0, LOW);
        digitalWrite(D3, LOW);
        digitalWrite(D4, LOW);
        connectCounter++;
        WiFi.disconnect();
        Serial.println("Connection failed (too long)");
        connectionFailed = true;
      } else {
        long time = millis();
        if (time > next_change) {
          digitalWrite(D0, !digitalRead(D0));
          digitalWrite(D3, !digitalRead(D3));
          digitalWrite(D4, !digitalRead(D4));
          next_change = time + 200;
          connectCounter++;
        }
      }
    } else if (connectCounter != -1) {
      Serial.print("Wifi connected: ");
      Serial.println(WiFi.localIP());
      digitalWrite(D0, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
      connectCounter = -1;
    }
  } else {
    connectionFailed = true;
  }

  // Fallback
  if (connectionFailed && !ap_enabled) {
    if (apfallback_enabled) {
      Serial.print("Access point fallback enabled: \"");
      Serial.print(config.hostname);
      Serial.print('"');

      if (WiFi.softAP(config.hostname, "")) {
        Serial.print(' ');
        Serial.println(WiFi.softAPIP());
        dns.start(53, "*", WiFi.softAPIP());
        ap_enabled = true;
      } else {
        Serial.println(" failed");
        delay(3000);
        ESP.restart();
      }
    } else {
      delay(3000);
      ESP.restart();
    }
  }
}
