#include <WiFi.h>
#include <WebServer.h>

WebServer server(80);

const char* ssid = "Rural-Water-Node";
const char* password = "health123";

#define PH_PIN        34
#define TDS_PIN       35
#define TURB_PIN      32
#define TEMP_PIN       4


int waterMode = 0;  
int tempMode = 1;  

float randRange(float a, float b) {
  return a + random(0, 1000) / 1000.0 * (b - a);
}

String getDataJSON() {
  float ph, tds, turb, temp;

  if (waterMode == 0) {
    ph = randRange(6.8, 7.4);
    tds = randRange(80, 250);
    turb = randRange(0.2, 1.5);
  } else if (waterMode == 1) {
    ph = randRange(6.0, 8.2);
    tds = randRange(300, 700);
    turb = randRange(2.0, 5.0);
  } else {
    ph = randRange(5.0, 9.5);
    tds = randRange(900, 2000);
    turb = randRange(6.0, 25.0);
  }

  if (tempMode == 0) temp = randRange(10, 15);
  else if (tempMode == 1) temp = randRange(22, 28);
  else if (tempMode == 2) temp = randRange(30, 35);
  else if (tempMode == 3) temp = randRange(40, 50);
  else temp = randRange(55, 65);

  return "{"
         "\"ph\":" + String(ph,2) + ","
         "\"tds\":" + String(tds,0) + ","
         "\"turbidity\":" + String(turb,2) + ","
         "\"temperature\":" + String(temp,1) +
         "}";
}

void handleData() {
  server.send(200, "application/json", getDataJSON());
}

void handleControl() {
  if (server.arg("key") != "admin123") {
    server.send(403, "text/plain", "Unauthorized");
    return;
  }
  waterMode = server.arg("water").toInt();
  tempMode = server.arg("temp").toInt();
  server.send(200, "text/plain", "Updated");
}

void setup() {
  Serial.begin(115200);
  randomSeed(analogRead(0));

  WiFi.softAP(ssid, password);

  server.on("/data", handleData);
  server.on("/control", handleControl);
  server.begin();
}

void loop() {
  server.handleClient();
}
