int leds[] = {4, 6, 8}; //digital
String valor; // XYZ -> 010,  110,   011 , 001

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i<3; i++){    
    pinMode(leds[i], OUTPUT);
  } 
  Serial.begin(9600); 
  Serial.setTimeout(100); 
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    valor = Serial.readString(); //cadena 
    for(int i = 0; i<3; i++){
      digitalWrite(leds[i], valor.charAt(i));
    }
  }
  delay(100);
}
