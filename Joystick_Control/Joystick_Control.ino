int x,y,k;

void setup() {
  // put your setup code here, to run once:
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  //......pinMode(4,INPUT);
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(4,HIGH);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  x=analogRead(A0);
  y=analogRead(A1);
  x=map(x,0,1023,0,640);
  y=map(y,0,1023,0,480);
  Serial.print(x);
  Serial.print(" ");
  Serial.println(y);
  delay(50);
}
