int index; 

int led1 = 6; 
int led2 = 7; 
int led3 = 8; 
int led4 = 9; 
int led5 = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);  

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){ //devuelve cuantos bytes hay en el buffer de entrada!
    index = Serial.readString().toInt(); 
    //suponinendo usuarios perfectos >.<
    
    digitalWrite(led1, 0);  
    digitalWrite(led2, 0);  
    digitalWrite(led3, 0);  
    digitalWrite(led4, 0);  
    digitalWrite(led5, 0);  

    switch(index){
      case 1:
        digitalWrite(led1, 1);  
        break;
      case 2:
        digitalWrite(led2, 1);  
        break;
      case 3:
        digitalWrite(led3, 1);  
        break;
      case 4:
        digitalWrite(led4, 1);  
        break;
      case 5:
        digitalWrite(led5, 1);  
        break;
    }
    

  }
  delay(100);
}
