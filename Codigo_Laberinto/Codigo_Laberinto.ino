#include "Motores.h"
#include "joystick.h"

Motor Motor;
Joystick joystick;

void setup() {
  Serial.begin(115200);
  Motor.begin();
  joystick.attach();//puedo entrgarle que pines, si no, lo hara por defer¿cto
}

void loop() {
  Motor.moverlaberintoX(joystick.lecturaX());
  Motor.moverlaberintoY(joystick.lecturaY());
  delay(80);
}

