#include <Stepper.h>


const float STEPS_PER_REV = 32;
const float GEAR_REDUCTION =  64; //need to check the gear revolution
const float STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_REDUCTION;
int StepsRequired=4;
int side_power=0;
int top_power=0;

Stepper stepperX(STEPS_PER_REV, 8,10,9,11);
Stepper stepperY(STEPS_PER_REV, 4,6,5,7);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    stepperX.setSpeed(700);
    stepperY.setSpeed(700);
    stepperX.step(StepsRequired);
    stepperY.step(StepsRequired);
    delay(5);
}
