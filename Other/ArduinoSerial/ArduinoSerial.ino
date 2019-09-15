#include <Stepper.h>

const float STEPS_PER_REV = 32;
const float GEAR_REDUCTION =  64; //need to check the gear revolution
const float STEPS_PER_OUT_REV = STEPS_PER_REV * GEAR_REDUCTION;
int StepsRequired;
int side_power=0;
int top_power=0;

Stepper stepperX(STEPS_PER_REV, 8,10,9,11);
Stepper stepperY(STEPS_PER_REV, 4,6,5,7);




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
    for (int i = 0; i< 8; i++){
      data[i]=Serial.read() - '0';
      delay(10);
      Serial.print(data[i]);
    }

    
    if (data[0]==1){
      //for x
      if (data[1] ==1){
        //positive:
        side_power = data[3]*10+data[4];
      }
      else{
        side_power = -1(data[3]*10+data[4]);
      }
    }
    if(data[4]==2) {
      //for y
        if (data[5]==1){//positive
          top_power = data[6]*10+data[7];
        }
        else{
          top_power = -1*(data[6]*10+data[7]);
        }
      
    }
    top_power = top_power*10;
    side_power = side_power*10;
    

  }
}
