#include <Stepper.h>


const float STEPS_PER_REV = 32;
const float GEAR_REDUCTION =  64; //need to check the gear revolution
const float STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_REDUCTION;
int StepsRequired;

Stepper stepperX(STEPS_PER_REV, 8,10,9,11);
//Stepper stepperY(Steps_PER_Rev, 4,6,5,7);
unsigned long incomingByte  = 0;


unsigned long readULongFromBytes() {
  union u_tag {
    byte b[4];
    unsigned long ulval;
  } u;
  u.b[0] = Serial.read();
  u.b[1] = Serial.read();
  u.b[2] = Serial.read();
  u.b[3] = Serial.read();
  return u.ulval;
}

void setup() {
   pinMode(13, OUTPUT);
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (!Serial) {  
    ; // wait for serial port to connect. Needed for native USB  
  } 
}


void loop() {
  
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    digitalWrite(13, HIGH); 
    incomingByte = readULongFromBytes();
    
    Serial.print(incomingByte,DEC);
    // read the incoming byte:
    /*
  if (incomingByte==15000){
    stepperX.setSpeed(800); //this variable determines the speed of the motor (top is around 700)
    StepsRequired = 10; //this determines how much it will move (maybe keep it as 5 or something)?
  //Right for positive, left for negative
    stepperX.step(StepsRequired);
  }
*/
  }
  delay(50);
  digitalWrite(13, HIGH); 
}
