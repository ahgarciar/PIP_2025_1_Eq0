int sensor1 = A0;
int sensor2 = A1;
int sensor3 = A2;
int sensor4 = A3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int v1, v2, v3, v4;

void loop() {
  // put your main code here, to run repeatedly:
  v1 = analogRead(sensor1);
  v2 = analogRead(sensor2);
  v3 = analogRead(sensor3);
  v4 = analogRead(sensor4);

  //Opcion 1
  /*
  Serial.println("S1-" + String(v1));
  Serial.println("S2-" + String(v2));
  Serial.println("S3-" + String(v3));
  Serial.println("S4-" + String(v4));
  */

  //Opcion 2 - TRAMA
  Serial.print("A"+String(v1) + "-" + String(v2) + "-" + String(v3) + "Z");


}
