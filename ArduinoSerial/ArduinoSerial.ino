#include <Stepper.h>

const float STEPS_PER_REV = 32;
const float GEAR_REDUCTION =  64; //need to check the gear revolution
const float STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_REDUCTION;
int StepsRequired;


Stepper stepperX(STEPS_PER_REV, 8,10,9,11);
//Stepper stepperY(Steps_PER_Rev, 4,6,5,7);



uint8_t data[8];

void setup() {
  // put your setup code here, to run once:
   pinMode(13, OUTPUT);
   pinMode(2, OUTPUT);

  // put your setup code here, to run once:
  Serial.begin(9600);

}


void loop() {
  digitalWrite(13, LOW);

  if (Serial.available()>7){//only when there are 
       digitalWrite(2, HIGH);
      delay(2000);
      digitalWrite(2, LOW);
      delay(10);
    digitalWrite(13, HIGH);
    for (int i = 0; i< 8; i++){
      data[i]=Serial.read();
      if (data[0] == 1){
        digitalWrite(2, HIGH);
        delay(2000);
        digitalWrite(2, LOW);
      }
      delay(10);
      Serial.print(data[i]);
      

    }



  }
}
