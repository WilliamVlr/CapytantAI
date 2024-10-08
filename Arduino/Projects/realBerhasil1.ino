/* rawSend.ino Example sketch for IRLib2
 *  Illustrates how to send a code Using raw timings which were captured
 *  from the "rawRecv.ino" sample sketch.  Load that sketch and
 *  capture the values. They will print in the serial monitor. Then you
 *  cut and paste that output into the appropriate section below.
 */
#include <IRLibSendBase.h>    //We need the base code
#include <IRLib_HashRaw.h>    //Only use raw sender

IRsendRaw mySender;
char val;

void setup() {
  Serial.begin(9600);
  delay(2000); 
  // while (!Serial); //delay for Leonardo
  Serial.println(F("Every time you press a key is a serial monitor we will send."));
}
/* Cut and paste the output from "rawRecv.ino" below here. It will 
 * consist of a #define RAW_DATA_LEN statement and an array definition
 * beginning with "uint16_t rawData[RAW_DATA_LEN]= {…" and concludes
 * with "…,1000};"
 */

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
/*
 * Cut-and-paste into the area above.
 */
   
void loop() {
  // val = Serial.read();
  // if (val == 'n'){
  //   mySender.send(rawData,RAW_DATA_LEN,36);//Pass the buffer,length, optionally frequency
  //   Serial.println(F("Sent signal."));
  //   val = 0;
  // }else{
  //   Serial.println(F("Command not recognized"));
  // }

  if (Serial.read() != -1) {
    //send a code every time a character is received from the 
    // serial port. You could modify this sketch to send when you
    // push a button connected to an digital input pin.
    mySender.send(rawData,RAW_DATA_LEN,36);//Pass the hbuffer,length, optionally frequency
    Serial.println(F("Sent signal."));
  }
}

