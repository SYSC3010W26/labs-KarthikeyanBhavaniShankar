# SYSC3010 – Lab 5: PiCam and Computer Vision

This folder contains my work for **Lab 5 – PiCam and Computer Vision**.  
The goal of this lab was to use the Raspberry Pi Camera to stream video, capture images, and build a simple computer-vision-based home security system using edge computing.

## What’s in this folder

### Web Streaming
- **webstreaming.py**  
  A Python script adapted from the Picamera2 MJPEG streaming example.  
  It streams live video from the Raspberry Pi camera to a web browser and displays my name and course code at the top of the page.

- **lab5-web-stream.png**  
  A screenshot of the live video stream showing the camera feed with me holding a paper that displays my name.

### Mini-Project: Computer Vision Security System

The **mini-project** folder contains a simple rule-based computer vision system that detects when a person enters the camera’s field of view and triggers a SenseHAT alarm.

#### mini-project/
- **main_rpi.py**  
  The main program that provides a command-line menu to:
  - Capture a background (empty room) image  
  - Arm the system and periodically capture test images  
  - Detect a person by comparing pixel differences between images  
  - Trigger a SenseHAT LED alarm when motion is detected  

- **helper_functions/**  
  Helper modules used by the main program:
  - `camera.py` – Handles image capture using the Picamera2 library  
  - `computer_vision.py` – Implements person detection using background subtraction and a threshold  
  - `sensehat.py` – Controls the SenseHAT LED alarm  
  - `__init__.py` – Allows the folder to be used as a Python package
  
- **lab5-miniproject.png**  
  A screenshot showing the mini-project running, including terminal output indicating a detected person and the SenseHAT LEDs flashing.
