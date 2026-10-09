# SentraCore System Architecture

## 1. Overview

SentraCore is a prototype that explores rule-based detection of suspicious network-event patterns and communicates alerts to an ESP32 microcontroller.

The initial implementation uses Python to process event data, USB Serial to transmit alerts, and Arduino C++ firmware to control an LED connected to the ESP32.

## 2. System Components

### A. Event Input

The Python application reads structured event records from a CSV file. The initial demonstration uses fictional sample data. Live network monitoring is a separate integration task.

### B. Detection Engine

The detection engine evaluates each event against a configurable rule. In the initial version, an event with a connection_count of 20 or greater is flagged for review.

This is a demonstration threshold, not a validated cyberattack detection threshold.

### C. Communication Interface

The Python application transmits ALERT or NORMAL messages to the ESP32 over USB Serial at 115200 baud.

### D. ESP32 Alert Module

The ESP32 reads incoming messages. On receiving ALERT, it activates the built-in LED for approximately three seconds. On receiving NORMAL, it switches the LED off.

## 3. Communication Flow

1. Load event records from the CSV file.
2. Process each record using the Python detection rule.
3. Print the event classification.
4. If a serial port is configured, transmit the corresponding message.
5. The ESP32 reads the message and controls its LED.
6. Compare expected and observed results during testing.

## 4. Data Flow

CSV event data → Python detection engine → USB Serial → ESP32 firmware → LED alert

## 5. Safety and Privacy

Use authorized network data only. The initial demonstration does not perform network scanning, intercept communications, or automatically block traffic.

## 6. Limitations

* Sample data is fictional.
* The initial rule is simplistic and may produce false positives or miss threats.
* CSV processing does not by itself constitute live network monitoring.
* USB Serial communication requires the correct port and compatible firmware.
* The LED is a demonstration alert, not proof that a real cyberattack has been identified.

## 7. Future Improvements

* Integrate a permitted network-event collector.
* Develop and evaluate additional detection rules.
* Add a buzzer or other physical alert if required.
* Record test results, detection limitations, and communication reliability.
* Explore a dashboard for understandable alerts.
