int GreenLED = 13;
int YellowLED = 12;
int RedLED = 11;

int WhiteLED1 = 9;
int WhiteLED2 = 10;

int Button1 = 7;
int Button2 = 6;

int Buzzer = 8;

bool ButtonPressed = false;

void setup()
{
    pinMode(GreenLED, OUTPUT);
    pinMode(YellowLED, OUTPUT);
    pinMode(RedLED, OUTPUT);

    pinMode(WhiteLED1, OUTPUT);
    pinMode(WhiteLED2, OUTPUT);

    pinMode(Button1, INPUT_PULLUP);
    pinMode(Button2, INPUT_PULLUP);

    randomSeed(analogRead(A0));
}

void loop()
{
    digitalWrite(GreenLED, HIGH);
    tone(Buzzer, 1000);
    delay(80);
    noTone(Buzzer);
    delay(900);
    digitalWrite(GreenLED, LOW);

    digitalWrite(YellowLED, HIGH);
    tone(Buzzer, 1000);
    delay(80);
    noTone(Buzzer);
    delay(900);
    digitalWrite(YellowLED, LOW);

    digitalWrite(RedLED, HIGH);
    tone(Buzzer, 1000);
    delay(80);
    noTone(Buzzer);
    delay(random(900, 4901));
    digitalWrite(RedLED, LOW);

    digitalWrite(WhiteLED1, HIGH);
    digitalWrite(WhiteLED2, HIGH);

    while (ButtonPressed == false)
    {
        if (digitalRead(Button1) == 0)
        {
            ButtonPressed = true;
            digitalWrite(WhiteLED2, LOW);
            tone(Buzzer, 2000);
            delay(500);
            noTone(Buzzer);
            delay(1500);
        }
        else if (digitalRead(Button2) == 0)
        {
            ButtonPressed = true;
            digitalWrite(WhiteLED1, LOW);
            tone(Buzzer, 2000);
            delay(500);
            noTone(Buzzer);
            delay(1500);
        }
    }
    digitalWrite(WhiteLED1, LOW);
    digitalWrite(WhiteLED2, LOW);
    ButtonPressed = false;
}