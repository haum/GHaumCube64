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
}

void loop() {
  led_nb = (led_nb + 1) % 3;
  digitalWrite(D0, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(leds[led_nb], LOW);
  delay(200);

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
}
