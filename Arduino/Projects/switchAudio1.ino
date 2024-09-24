#include <IRLibSendBase.h>    //We need the base code
#include <IRLib_HashRaw.h>

IRsendRaw mySender;

const int kamar = 4;
const int balkon = 5;
const int kipas = 6;

char val;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(2000); 
  pinMode(kamar, OUTPUT);
  pinMode(balkon, OUTPUT);
  pinMode(kipas, OUTPUT);

  digitalWrite(kamar, HIGH);
  digitalWrite(balkon, HIGH);
  digitalWrite(kipas, HIGH);
}

#define RAW_DATA_LEN 68
uint16_t rawData[RAW_DATA_LEN]={
	8986, 4506, 566, 1722, 538, 1694, 562, 566, 
	566, 562, 570, 562, 566, 566, 566, 562, 
	570, 1690, 566, 1694, 566, 562, 570, 1690, 
	566, 562, 570, 1690, 566, 562, 570, 1690, 
	570, 562, 566, 562, 570, 562, 570, 562, 
	566, 566, 566, 1690, 594, 538, 566, 566, 
	590, 1666, 570, 1690, 566, 1690, 570, 1690, 
	566, 1694, 566, 562, 570, 1690, 566, 1694, 
	566, 562, 566, 1000};

void loop() {
  // put your main code here, to run repeatedly:
  val = Serial.read();
  if(val == 'e'){
    digitalWrite(kamar, LOW);//Nyalakan lampu kamar
  } else if(val == 'f'){
    digitalWrite(kamar, HIGH);//matikan lampu kamar
  } else if(val == 'a'){
    digitalWrite(balkon, LOW);//nyalakan lampu balkon
  } else if(val == 'b'){
    digitalWrite(balkon, HIGH);//matikan lampu balkon
  } else if(val == 's'){
    digitalWrite(kipas, LOW);//nyalakan kipas angin
  } else if(val == 't'){
    digitalWrite(kipas, HIGH);//matikan kipas angin
  } else if (val == 'p'){//nyalakan proyektor
    mySender.send(rawData,RAW_DATA_LEN,36);//Pass the buffer,length, optionally frequency
    Serial.println(F("Sent signal."));
  } else if (val == 'q'){//matikan proyektor
    mySender.send(rawData,RAW_DATA_LEN,36);
    Serial.println(F("Sent signal once."));
    delay(2000);
    mySender.send(rawData,RAW_DATA_LEN,36);
    Serial.println(F("Sent signal second."));
  }
  else{
    // Serial.println(F("Command not recognized"));
  }
  val = '0';
}
