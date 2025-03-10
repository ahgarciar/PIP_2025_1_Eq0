//pines.   1.   2.   3.  
//        GND   A0   5V
//Pin 1 y 3 son intercambiables (no importa cual es cual)
//Son los extremos del potenciometro

int pot = A0; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(pot);
  Serial.println(valor);
  delay(100);
}
