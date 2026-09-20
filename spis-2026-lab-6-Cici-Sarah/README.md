# SPIS 2026 — Lab 6: Raspberry Pi (starter code)

Cici Xing & Sarah Xu: Lab 6: Robotics 

Starter code for **Lab 6**. Full instructions are on the course site:
**FoCS Labs → Lab 6 (2026)**.

This repository is created for your pair automatically when one of you accepts the
Lab 6 assignment on Classroom 50. You then develop and run this code **on the
Raspberry Pi** and push your changes back here so your partner and the instructional
staff can see them.

## Files

| File | What it is |
| --- | --- |
| `00_test.py` | Quick "Hello, World!" to check Python runs on the Pi |
| `01_blinking_LED.py` | Blink an LED on GPIO 16 |
| `02_buttonLED.py` | Read a button on GPIO 20 |
| `03_servo.py` | Drive a servo on GPIO 25 with PWM |
| `04_timing.py` | Non-blocking delays without `time.sleep()` |
| `05_ultrasound.py` | Measure distance with an HC-SR04 on GPIO 18/24 |
| `06_picam_preview.py` | Confirm the camera works (5-second preview) |
| `06_picam_video.py` | Live video + a numpy image manipulation |

Pin numbers use the **BCM** numbering scheme (`GPIO.setmode(GPIO.BCM)`).

## Getting this code onto your Raspberry Pi

You will do this from the Pi itself. Open a terminal and clone your team's repo
(replace the URL with the one shown by the green **Code** button on your repo page):

```bash
git clone https://github.com/ucsd-cse-spis-2026/spis-2026-lab6-<your-repo>.git
cd spis-2026-lab6-<your-repo>
```

Run a program:

```bash
python 01_blinking_LED.py
```

Stop a running program with **Ctrl+C**.

## Saving your work back to GitHub

Push often, and definitely at the end of the session:

```bash
git add -A
git commit -m "describe what you changed"
git push
```


## What you'll submit

You'll create solution files as you go (e.g. `01_blinking_LED_sol.py`,
`02_buttonLED_sol1.py`, `03_servo_sol1.py`, …). The lab writeup tells you exactly
which files to create and commit for each part.
