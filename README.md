# Motion-Detector
This project implements a motion detection system using a camera. The system captures video frames from the webcam, converts them to grayscale, and then applies a threshold to detect motion. If motion is detected, the system triggers an alarm and sends an email with an image of the motion.

**Features**
Detects motion using a webcam
Triggers an alarm when motion is detected
Sends an email with an image of the motion
Requirements
1) camera
2) Python 3
3) OpenCV library
4) smtplib library

**Technical Details**
The motion detector uses the following techniques:

**Video capture:** The system uses the OpenCV library to capture video frames from the webcam.
**Grayscale conversion:** The system converts video frames to grayscale to reduce noise and simplify motion detection.
**Thresholding:** The system applies a threshold to the grayscale images to detect motion.
**Alarm:** The system triggers an alarm when motion is detected.
**Email notification:** The system sends an email with an image of the motion when motion is detected.

**Future Work**
The motion detector could be improved in the following ways:

**Object detection:** The system could be extended to detect objects in the video frames.
**Object tracking:** The system could be extended to track objects in the video frames.
**Image classification:** The system could be extended to classify objects in the video frames.
**Video analytics:** The system could be extended to perform video analytics, such as counting people or vehicles.
