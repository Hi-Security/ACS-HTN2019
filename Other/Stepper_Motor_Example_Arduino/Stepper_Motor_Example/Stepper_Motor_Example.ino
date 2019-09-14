#include <Stepper.h>

const float STEPS_PER_REV = 32;
const float GEAR_REDUCTION =  64; //need to check the gear revolution
const float STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_REDUCTION;

int StepsRequired;

Stepper stepperX(STEPS_PER_REV, 8,10,9,11);
Stepper stepperY(Steps_PER_Rev, 4,6,5,7);

void setup (){
  
}

void loop(){
  stepperX.setSpeed(1); //this variable determines the speed of the motor (top is around 700)
  StepsRequired = 4; //this determines how much it will move (maybe keep it as 5 or something)?
  //Right for positive, left for negative
  stepperX.step(StepsRequired);
  delay(50);
  
  
}
