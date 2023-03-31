const byte led = 2;

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  delay(1000);
}

void loop() {
  if(Serial.available()){
    char dato = Serial.read();
    if(dato== 'w'){
      digitalWrite(led, 1);
      delay(500);
      digitalWrite(led, 0);
      delay(500);
      digitalWrite(led, 1);
      delay(500);
      digitalWrite(led, 0);
    }
    else if(dato== 's'){
      digitalWrite(led, 1);
      delay(1000);
      digitalWrite(led, 0);
    }
    else if(dato== 'a'){
      digitalWrite(led, 1);
      delay(1000);
      digitalWrite(led, 0);
      delay(1000);
      digitalWrite(led, 1);
      delay(1000);
      digitalWrite(led, 0);
    }
    else if(dato== 'd'){
      digitalWrite(led, 1);
      delay(2000);
      digitalWrite(led, 0);
    }
    else{
      digitalWrite(led, 1);
      delay(200);
      digitalWrite(led, 0);
      delay(200);
      digitalWrite(led, 1);
      delay(200);
      digitalWrite(led, 0);
      delay(200);
      digitalWrite(led, 1);
      delay(200);
      digitalWrite(led, 0);
      delay(200);
      digitalWrite(led, 1);
    }
  }

}
