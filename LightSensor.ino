const int LDR = A3;
const int LED = 4;

int input_val = 0;

void setup()
{
  Serial.begin(115200);
  pinMode(LED,OUTPUT);
}

void loop()
{
  input_val = analogRead(LDR);

  if(input_val > 300)
  {
    digitalWrite(LED,HIGH);
  }
  else
  {
    digitalWrite(LED,LOW);
  }
  Serial.println(input_val);
  delay(1000);
  
}
