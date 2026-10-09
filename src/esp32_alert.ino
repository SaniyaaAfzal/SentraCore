
const int ALERT_LED = LED_BUILTIN;

String receivedMessage = "";
unsigned long alertStartedAt = 0;
const unsigned long ALERT_DURATION_MS = 3000;

bool alertActive = false;

void setup() {
  pinMode(ALERT_LED, OUTPUT);
  digitalWrite(ALERT_LED, LOW);

  Serial.begin(115200);
  receivedMessage.reserve(32);

  Serial.println("SentraCore ESP32 alert module ready");
}

void handleMessage(String message) {
  message.trim();

  if (message == "ALERT") {
    digitalWrite(ALERT_LED, HIGH);
    alertStartedAt = millis();
    alertActive = true;
    Serial.println("ACK: ALERT");
  } else if (message == "NORMAL") {
    digitalWrite(ALERT_LED, LOW);
    alertActive = false;
    Serial.println("ACK: NORMAL");
  }
}

void loop() {
  while (Serial.available() > 0) {
    char incoming = static_cast<char>(Serial.read());

    if (incoming == '\n') {
      handleMessage(receivedMessage);
      receivedMessage = "";
    } else if (incoming != '\r') {
      if (receivedMessage.length() < 32) {
        receivedMessage += incoming;
      } else {
        receivedMessage = "";
      }
    }
  }

  if (alertActive &&
      millis() - alertStartedAt >= ALERT_DURATION_MS) {
    digitalWrite(ALERT_LED, LOW);
    alertActive = false;
  }
}
