int v; 

void setup() {
  // put your setup code here, to run once:
  v = 0;
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println("hola");
  //Serial.println(v);
  
  Serial.println("Valor: " + String(v));  
  v+=1;
  delay(100);

}
