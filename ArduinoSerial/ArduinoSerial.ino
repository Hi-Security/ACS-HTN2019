#include <Stepper.h>



const float STEPS_PER_REV = 32;
const float GEAR_REDUCTION =  64; //need to check the gear revolution
const float STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_REDUCTION;
int StepsRequiredX = 15;
int StepsRequiredY = 15;
//for opposite direction, use -1*StepsRequired
int side_power=0;
int top_power=0;
int hundred;
int ten;
int single;
int stepper_X_power = 0;
int stepper_Y_power = 0;
Stepper stepperX(STEPS_PER_REV, 8,10,9,11);
Stepper stepperY(STEPS_PER_REV, 4,6,5,7);
char power = ' ';

String readString;

void CharParser(String data){
  if (data[0]=='P'){//positive
    StepsRequiredX = abs(StepsRequiredX);   
  }
  else{
    StepsRequiredX = abs(StepsRequiredX)*-1;
  }
  if(data[4] =='P'){
    StepsRequiredY = abs(StepsRequiredY);     
  }
  else{
    StepsRequiredY = abs(StepsRequiredY)*-1;     
  }
  
  hundred = data[1] -'0';
  ten = data[2] -'0';
  single = data[3] -'0';
  stepper_X_power = hundred*100+ten*10+single;
  hundred = data[5] -'0';
  ten = data[6] -'0';
  single = data[7] -'0';
  stepper_Y_power = hundred*100+ten*10+single;
  //Serial.write(stepper_X_power);
  //Serial.write(stepper_Y_power);
  driver(stepper_X_power, stepper_Y_power);
}

void driver(int X_power, int Y_power){
  stepperX.setSpeed(X_power);
  stepperY.setSpeed(Y_power);
  stepperX.step(StepsRequiredX);
  stepperY.step(StepsRequiredY);
}


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);


}

void loop() {
 while(!Serial.available()) {}
  // serial read section
  while (Serial.available())
  {
    if (Serial.available() >0)
    {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }

  if (readString.length() >=7)
  {
//    Serial.print("Arduino received: ");  
    //Serial.println(readString); //see what was received
    //Serial.flush();

//steven, put your code here
    CharParser(readString);


    readString = "";
  }

  delay(1);

  // serial write section

  //char ard_sends = '1';
//  Serial.print("Arduino sends: ");
//  Serial.println(ard_sends);
//  Serial.print("\n");

  
}
