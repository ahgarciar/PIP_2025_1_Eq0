int valores[3] = {0, 0 ,0};
int sensores[3] = {A0, A1, A2}; //lm35, dht11, LDR, HCSR04, PIR,....
int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
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
  Serial.println(cadena);
  
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
    digitalWrite(led, v);
  }
  
  delay(100);
}
