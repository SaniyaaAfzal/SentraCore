# SentraCore Test Plan

## Objective

Verify the rule-based event detector and USB Serial alert prototype.

## Test Cases

| Test ID | Test                                | Expected Result                                   |
| ------- | ----------------------------------- | ------------------------------------------------- |
| T01     | Process an event with count 3       | NORMAL                                            |
| T02     | Process an event with count 19      | NORMAL                                            |
| T03     | Process an event with count 20      | ALERT                                             |
| T04     | Process an event with count 25      | ALERT                                             |
| T05     | Process an invalid connection count | ValueError is raised                              |
| T06     | Send ALERT to a connected ESP32     | LED activates                                     |
| T07     | Send NORMAL to a connected ESP32    | LED switches off                                  |
| T08     | Disconnect the serial cable         | Communication is unavailable and must be reported |

## Test Environment

* Computer with Python 3 installed
* ESP32 development board
* USB data cable
* Arduino IDE
* Python unittest framework
* Fictional CSV event data

## Results Record

Record the actual outcome of each test after running it. Do not mark a test as passed until the observed result matches the expected result.

| Test ID | Actual Result | Status     | Notes                   |
| ------- | ------------- | ---------- | ----------------------- |
| T01     | Pending       | Not tested |                         |
| T02     | Pending       | Not tested |                         |
| T03     | Pending       | Not tested |                         |
| T04     | Pending       | Not tested |                         |
| T05     | Pending       | Not tested |                         |
| T06     | Pending       | Not tested | Requires ESP32          |
| T07     | Pending       | Not tested | Requires ESP32          |
| T08     | Pending       | Not tested | Verify failure handling |

## Limitations

These tests validate a simple rule-based prototype, not the ability to identify all cyberattacks. USB Serial disconnection handling, physical alert reliability, and live network monitoring require additional validation.
