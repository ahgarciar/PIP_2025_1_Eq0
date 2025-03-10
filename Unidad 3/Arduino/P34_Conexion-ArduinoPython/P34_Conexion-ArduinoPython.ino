int contador;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  contador = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Alumnos: " + String(contador++));
  delay(1000);
}
