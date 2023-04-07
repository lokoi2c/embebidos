#include"Motores.h"

/*Motor::Motor()
{
¿que sucede? ¿por que me dice que estoy redefiniendo el constructor
}**/
Servo servoX, servoY;//creo los objetos servo
  int gradosy = 90;
  int servo = 80;
  
  #define equilibrioX 80
  #define equilibrioY 88

void Motor::moverlaberintoY(int valor){
  if(valor > 2100){ 
    gradosy ++;
    if(gradosy > (equilibrioY + 20)) gradosy=(equilibrioY + 20);
    }
  else if(valor < 1700){ 
    gradosy --;
    if(gradosy < (equilibrioY - 20)) gradosy=(equilibrioY - 20);
    }
  else gradosy = 90;
  servoY.write(gradosy); Serial.println("grados YS: " + String(gradosy));
}
void Motor::moverlaberintoX(int valor){

   if(valor > 2100){ 
    servo ++;
    if(servo > (equilibrioX+20)) servo=(equilibrioX+20);
    }
  else if(valor < 1700){ 
    servo --;
    if(servo < (equilibrioX-20)) servo=(equilibrioX-20);
    }
  else servo = equilibrioX;

  servoX.write(servo); Serial.println("grados x: " + String(servo));

}

void Motor::begin(){
  servoX.attach(pinMotorX);
  servoY.attach(pinMotorY);
  delay(100);
  servoX.write(90);
  servoY.write(90);
}

