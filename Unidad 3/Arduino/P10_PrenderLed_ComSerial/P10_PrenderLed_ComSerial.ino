int respuesta; 
int led = 13; //led de prueba

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){ //devuelve cuantos bytes hay en el buffer de entrada!
    respuesta = Serial.readString().toInt(); 
    //suponinendo usuarios perfectos >.<
    
    digitalWrite(led, respuesta);

  }
  delay(100);
}
