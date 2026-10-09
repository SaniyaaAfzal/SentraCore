# SentraCore

### Smart Cyber Threat Detection and Alert System

## 1. Project Overview

SentraCore is a low-cost cybersecurity prototype designed to identify suspicious network activity and provide physical alerts. It combines computer-based network monitoring with an ESP32 microcontroller to make cyber threat awareness more accessible.

## 2. Problem Statement

Many students, individuals, and small organizations lack affordable and easy-to-understand tools for monitoring suspicious network activity. SentraCore explores a simple, accessible approach to threat detection and alerting.

## 3. Objectives

* Monitor permitted network activity.
* Identify suspicious patterns using defined detection rules.
* Communicate alerts to an ESP32.
* Activate a physical alert mechanism.
* Evaluate the prototype through controlled tests.

## 4. Hardware Components

* ESP32-WROOM development board
* Breadboard
* PIR motion sensor, if used in the implemented design
* Jumper wires
* USB Type-C data cable
* Physical alert components, according to the final circuit

## 5. Software and Technologies

* ESP32 firmware development environment
* Python or another language used by the implemented monitoring software
* Serial or other implemented communication interface
* Detection rules and testing utilities

*Update this section to match the actual software and interfaces used.*

## 6. System Workflow

1. Collect permitted network activity.
2. Process the observed events.
3. Apply the implemented detection rules.
4. Send an alert when a configured condition is met.
5. Receive the alert on the ESP32.
6. Activate the connected warning mechanism, if configured.

## 7. Repository Structure

* `src/` — application and firmware source code
* `docs/` — architecture and design documentation
* `sample_data/` — safe sample events
* `tests/` — validation and test cases

## 8. Setup and Usage

Detailed installation, configuration, wiring, and execution instructions will be documented after the source code and hardware connections are finalized.

## 9. Testing

The project will be evaluated using controlled test cases for normal activity, suspicious-pattern detection, communication reliability, and alert activation. Results will be documented as testing is completed.

## 10. Social Impact

SentraCore aims to support cybersecurity awareness by exploring an affordable, accessible method of identifying suspicious activity and providing understandable alerts.

## 11. Current Status

Prototype development and validation are ongoing. Implemented features, test results, limitations, and future improvements will be documented as the project progresses.

## 12. License

A license will be added once the team confirms the intended terms for sharing and reuse.
