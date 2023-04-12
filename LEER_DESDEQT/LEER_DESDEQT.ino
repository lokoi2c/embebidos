#include "serialqt.h"

serialQT serialQT1;


void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
//char dato = serialCaracter();
int valorx = 0;
 int valory = 0;
    if(Serial.available()){
        char dato = Serial.read();
        valorx = serialQT1.serialX(dato);
        valory = serialQT1.serialY(dato);
    }
        //Serial.println("valorx: " + String(valorx) + "  valorY: " + String(valory));
}




