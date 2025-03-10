int led = 6; //digital
int valor;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600); 
  Serial.setTimeout(100); 
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    valor = Serial.readString().toInt();
    digitalWrite(led, valor);
  }
  delay(100);
}
