int valores[] = {0, 0 ,0};
int sensores[] = {A0, A1, A2}; //lm35, dht11, LDR, HCSR04, PIR,....

//actuadores
int leds[] = {10,11,12};

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i<3; i++){
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100);
}

String cadena; 
void loop() {
  // put your main code here, to run repeatedly:
  cadena ="";
  for(int i  = 0; i<3; i++){
    valores[i] = analogRead(sensores[i]);
    cadena += String(valores[i]) + "-";
  }
  //Serial.println(cadena);
  
  if(Serial.available()>0){
    String v = Serial.readString();
    int a = v.charAt(0)-48;
    int b = v.charAt(1)-48;   
    digitalWrite(leds[a-1], b);
    Serial.println(String(a)+ "  " + String(b));
  }
  
  delay(100);
}
