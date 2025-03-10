String respuesta; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){ //devuelve cuantos bytes hay en el buffer de entrada!
    respuesta = Serial.readString(); //lee todos los caracteres que le sean posible
    //hasta alcanzar el tiempo limite (timeout). Por defecto timeout = 1 segundo :D
    
    Serial.println(respuesta); //echo!

  }

}
