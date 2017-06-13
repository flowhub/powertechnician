int pinButton = 2;
int LED = 3;
int LE = 4;
int stateLED = LOW;
int stateLE = LOW;
int stateButton;
int previous = LOW;
long time = 0;
long debounce = 200;

void setup() {
  pinMode(pinButton, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(LE, OUTPUT);

}

void loop() {
  stateButton = digitalRead(pinButton);  
  if(stateButton == HIGH && previous == LOW && millis() - time > debounce) {
    if(stateLED == HIGH){
      stateLED = LOW,
      stateLE = LOW;
    } else {
       stateLED = HIGH,
       stateLE = HIGH; 
    }
    time = millis();
  }
  digitalWrite(LED, stateLED);
  digitalWrite(LE, stateLE);
  previous == stateButton;
}
