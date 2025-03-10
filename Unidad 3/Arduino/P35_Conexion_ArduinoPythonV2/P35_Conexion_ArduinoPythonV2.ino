int pot = A0;
int valor;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  
}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(pot);
  Serial.println(valor);
  delay(250);
}
