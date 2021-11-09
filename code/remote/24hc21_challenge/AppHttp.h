#ifndef APPHTTP_H
#define APPHTTP_H

#include "AppConfig.h"
#include <ESP8266WebServer.h>

class AppHttp {
  public:
	AppHttp(AppConfig &c, ESP8266WebServer &s);
	static bool testCaptive(ESP8266WebServer &server);

  private:
	ESP8266WebServer &server;
	AppConfig &config;

	void handleNotFound();
	void handleRoot();
	void handleConfig();
};

#endif
