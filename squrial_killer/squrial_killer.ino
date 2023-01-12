/*
CODE HERE
Array of HC-SR04 ultrasonic sensors
*/
#include <Adafruit_NeoPixel.h>
#define PIN_NEO_PIXEL  9  // Arduino pin that connects to NeoPixel
#define NUM_PIXELS     10  // The number of LEDs (pixels) on NeoPixel
Adafruit_NeoPixel NeoPixel(NUM_PIXELS, PIN_NEO_PIXEL, NEO_GRB + NEO_KHZ800);

#include <ArduinoJson.h>
StaticJsonDocument<200> doc;

//Sonar 1
int echoPin1 =11;
int initPin1 =12;
int distance1 =0; 

//Sonar 2
int echoPin2 =14;
int initPin2 =15;
int distance2 =0;

//Sonar 3
int echoPin3 =17;
int initPin3 =18;
int distance3 =0;

int piezo = 6;
void setup() 
{
  NeoPixel.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)

  pinMode(initPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(initPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(initPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  pinMode(5, OUTPUT);
  Serial.begin(9600);
  
}

void loop() 
{
  int pixel;
  
  distance1 = getDistance(initPin1, echoPin1);
  printDistance(1, distance1);
  //Serial.println(distance1);
  delay(150);
  
  distance2 = getDistance(initPin2, echoPin2);
  printDistance(2, distance2);
  //Serial.println(distance2);
  delay(150);
  
  distance3 = getDistance(initPin3, echoPin3);
  printDistance(3, distance3);
  //Serial.println(distance3);
  delay(150);
  
  if (distance1 <= 3 || distance2 <0 || distance3 <= 3)
  {
   for (int pixel = 0; pixel < NUM_PIXELS; pixel++) 
   // For loop to turn on each pixel
   {  
    NeoPixel.setPixelColor(pixel, NeoPixel.Color(255, 0, 0));
    // .Color(Red, Green, Blue)  
    // It only takes effect if pixels.show() is called
    NeoPixel.setBrightness(50); 
    // .setBrightness takes in a value from 0 to 255
   }
   NeoPixel.show();
   tone(piezo, 15000, 500);
  }
  else 
  {
    NeoPixel.clear();
    NeoPixel.show();
  }
}

int getDistance (int initPin, int echoPin)
{
  digitalWrite(initPin, HIGH);
  delayMicroseconds(10); 
  digitalWrite(initPin, LOW); 
  unsigned long pulseTime = pulseIn(echoPin, HIGH); 
  int distance = pulseTime/58;
  return distance;
}

void printDistance(int id, int dist)
{
  /*
  Serial.print(id);
  Serial.print(": ");
  Serial.print(dist);
  Serial.print(" cm");  
  */
  doc["sensor"] = id;
  doc["distance"] = dist;
  serializeJsonPretty(doc, Serial);
}

