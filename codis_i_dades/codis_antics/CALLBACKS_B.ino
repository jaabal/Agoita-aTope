#include <Firmata.h>

#define TIME_A0 1000  // mil.lisegons 
#define TIME_A1 1000
#define TIME_A2 1000
#define TIME_A3 1000
#define TIME_A4 1000
#define TIME_A5 1000

#define TIME_A0_1 10  // microsegons 
#define TIME_A1_1 100
#define TIME_A2_1 10
#define TIME_A3_1 100
#define TIME_A4_1 10
#define TIME_A5_1 10

#define TIME_A5_2 1000 //micros

#define N_SAMPLES0 10
#define N_SAMPLES1 50
#define N_SAMPLES2 100
#define N_SAMPLES3 100
#define N_SAMPLES4 100
#define N_SAMPLES5 100
#define N_SAMPLES5_2 100

#define N_SAMPLES 22 // Té a veure amb el màxim d'A5

#define a2m 725 // (1023*Vcc/2/aref) ~ (1023*4.68/2/3.3)
//#define a5m 725 // (1023*Vcc/2/aref) ~ (1023*4.68/2/3.3)

int max_val;
int min_val;
int n;
unsigned long current_val;
int current_val5[N_SAMPLES];
unsigned long previousMillis,currentMillis;
int a5m;

void reportAnalogCallback(byte pin, int value){
  current_val = 0;
    
  switch(pin){
    
    case 0:
      analogReference(EXTERNAL);
      Firmata.sendAnalog(pin, analogRead(pin));
      delay(TIME_A0);
      for(int i=0; i<N_SAMPLES0; i++){
        delayMicroseconds(TIME_A0_1);
        current_val = current_val+analogRead(pin);
      }
      current_val = current_val / N_SAMPLES0;
      Firmata.sendAnalog(pin, current_val);
      break;

    case 1:
      analogReference(EXTERNAL);
      Firmata.sendAnalog(pin, analogRead(pin));
      delay(TIME_A1);
      for(int i=0; i<N_SAMPLES1; i++){
        delayMicroseconds(TIME_A1_1);
        current_val = current_val+analogRead(pin);
      }
      current_val = current_val / N_SAMPLES1;
      Firmata.sendAnalog(pin, current_val);
      break;
      
    case 2:
      analogReference(EXTERNAL);
      Firmata.sendAnalog(pin, analogRead(pin));
      delay(TIME_A2);
      for(int i=0; i<N_SAMPLES2; i++){
        delayMicroseconds(TIME_A2_1);
        unsigned long ra2=analogRead(pin);
        current_val = current_val+sq(ra2-a2m);//cal fer el quadrat de cada lectura menys el valor de 2.5Vaprox
      }
      current_val = (int)sqrt((float)current_val / (float)N_SAMPLES2);
      Firmata.sendAnalog(pin, current_val);
      break;

    case 3:
      analogReference(EXTERNAL);
      Firmata.sendAnalog(pin, analogRead(pin));
      delay(TIME_A3);
      for(int i=0; i<N_SAMPLES3; i++){
        delayMicroseconds(TIME_A3_1);
        current_val = current_val+analogRead(pin);
      }
      current_val = current_val / N_SAMPLES3;
      Firmata.sendAnalog(pin, current_val);
      break;

    case 4:
      analogReference(EXTERNAL);
      Firmata.sendAnalog(pin, analogRead(pin));
      delay(TIME_A4);
      for(int i=0; i<N_SAMPLES4; i++){
        delayMicroseconds(TIME_A4_1);
        unsigned long ra4 = analogRead(pin);
        current_val = current_val+sq(ra4); //Cal fer el quadrat de cada lectura
      }
      current_val = (int)sqrt((float)current_val / (float)N_SAMPLES4);
      Firmata.sendAnalog(pin, current_val);
      break;  

    case 5:
      analogReference(EXTERNAL);
      Firmata.sendAnalog(pin, analogRead(pin));
      delay(TIME_A5);
      max_val = analogRead(pin);
      min_val = max_val;
      
      for(int i=0; i<N_SAMPLES5; i++){
        delay(1);
        current_val = analogRead(pin);
        if (current_val > max_val){
          max_val = current_val;
        }
        if (current_val < min_val){
          min_val = current_val;
        }
      }
      a5m = (max_val+min_val)/2;
      
      for(int i=0; i<N_SAMPLES5_2; i++){
        delayMicroseconds(TIME_A5_2);
        unsigned long ra5=analogRead(pin);
        current_val = current_val+sq(ra5-a5m);//cal fer el quadrat de cada lectura menys el valor de 2.5Vaprox
      }
      current_val = (int)sqrt((float)current_val / (float)N_SAMPLES5_2);
      Firmata.sendAnalog(pin, current_val);
      
      
      //Firmata.sendAnalog(pin, (max_val+min_val)/2);
      
  }
    /*
    case 5:
      analogReference(EXTERNAL);
      Firmata.sendAnalog(pin, analogRead(pin));
      delay(TIME_A5);
      
      max_val = analogRead(pin);

      n = 0;
      for (int i=0; i<N_SAMPLES;i++){
        current_val5[i] = 0;
      }
      
      previousMillis = millis();
      while(n < N_SAMPLES5){
        currentMillis = millis();
        if (currentMillis - previousMillis > 40*n) {
          for(int i=0; i<N_SAMPLES; i++){
            delay(1);
            current_val5[i] = current_val5[i] + analogRead(pin);
          }
          n=n+1;
        }
      }
      for (int i=0; i<N_SAMPLES; i++){
        current_val5[i] = current_val5[i] / N_SAMPLES5;
      }
      max_val = current_val5[0];
      min_val = max_val;
      for (int i=1; i<N_SAMPLES; i++){
        if (current_val5[i] > max_val){
          max_val = current_val5[i];
        }
        if (current_val5[i] < min_val){
          min_val = current_val5[i];
        }
      }

      a5m = (max_val+min_val/2);
      
      Firmata.sendAnalog(pin, a5m);
      //Firmata.sendAnalog(pin, current_val);
      break;
  }  */
}

void setup(){
  Firmata.setFirmwareVersion(FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION);
  Firmata.attach(REPORT_ANALOG, reportAnalogCallback);
  Firmata.begin(57600);
}

void loop(){
  // Si no hi ha available i processInput no funciona!
  while (Firmata.available()) // Comprova si esta rebent dades (available mira el nombre de bytes del stream input data)
    Firmata.processInput();     // Llegeix les dades rebudes
}

