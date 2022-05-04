#include <Servo.h>                           // Include servo library
 
Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

  int forwardFlag = 5;
  int rightFlag = 7;
  int leftFlag = 9;
  int stopFlag = 11;

  #define echoPin 2 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 3 //attach pin D3 Arduino to pin Trig of HC-SR04

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

void right() {
  servoLeft.attach(12);                      // Attach left signal to pin 13
  servoRight.attach(13);
  servoLeft.writeMicroseconds(1600);
  servoRight.writeMicroseconds(1600);
  delay(1000);
  servoLeft.detach();
  servoRight.detach();
}

void left() {
  servoLeft.attach(12);                      // Attach left signal to pin 13
  servoRight.attach(13);
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
  delay(700);
  servoLeft.detach();
  servoRight.detach();
}

void forward() {
  servoLeft.attach(12);                      // Attach left signal to pin 13
  servoRight.attach(13);
  servoLeft.writeMicroseconds(1600);
  servoRight.writeMicroseconds(1400);
  delay(300);
  servoLeft.detach();
  servoRight.detach();
}

void stopMoving(int counter) {
  servoLeft.detach();
  servoRight.detach();
  delay(counter);
}

void setup() {                                // Built in initialization block
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  Serial.println("Ultrasonic Sensor HC-SR04 Test"); // print some text in Serial Monitor
  Serial.println("with Arduino UNO R3");
}  
 
void loop() {                                 // Main loop auto-repeats


  //JSDFGJK;SDFHLGJK

  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  //FADJHYFGASDHLG

  if (distance > 20) {
    forward();
  }

  else if (distance < 20) {
    stopMoving(900);
    right();
  }

  while (digitalRead(leftFlag) == HIGH) {
    left();
  }

  while (digitalRead(stopFlag) == HIGH) {
    stopMoving(900);
  }

  //forward();
  //stopMoving(500);
  //right();
  //stopMoving(500);
  /*servoLeft.writeMicroseconds(1300);         // Pin 13 clockwise
  servoRight.writeMicroseconds(1300);        // Pin 12 clockwise
  delay(3000);                               // ..for 3 seconds
  servoLeft.writeMicroseconds(1700);         // Pin 13 counterclockwise
  servoRight.writeMicroseconds(1700);        // Pin 12 counterclockwise
  delay(3000);                               // ..for 3 seconds
  servoLeft.detach();         // Pin 13 stay still
  servoRight.detach();        // Pin 12 stay still*/
}
