import cv2
import imutils
import datetime
import threading
import winsound
import smtplib
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)


alarm = False
alarm_mod = False
alarm_counter = 0

motion_frame = None
now = datetime.datetime.now()


def beep_alarm():
    global alarm
    for _ in range(1):
        if not alarm_mod:
            break
        print("----------> Alarm <----------")
        winsound.Beep(1500, 1000)
    alarm = False


def send_email():
    global motion_frame

    message = MIMEMultipart()
    message["From"] = "motion.detector.v8@gmail.com"
    message["To"] = "ayhamasfoor1@gmail.com"
    message["Subject"] = "Motion Detection Alert"

    message_body = MIMEText(f"Dear Ayham Asfoor,\nDay:Sunday\nDate:{date.today()}\nTime:{now.strftime('%H:%M:%S')}\n\nThis email is to inform you that motion has been detected in your monitored area.\nThe motion detection system captured an image of the motion and attached it to this email.\nPlease review the image to see what triggered the alarm.\n\nSincerely,\nMotion Detection System", "plain")
    message.attach(message_body)

    if motion_frame is not None:
        image_data = cv2.imencode('.jpg', motion_frame)[1].tobytes()
        image = MIMEImage(image_data, name='motion.jpg', subtype='jpeg')
        message.attach(image)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("motion.detector.v8@gmail.com", "jvtv btad nvvx txnq")
        server.sendmail("motion.detector.v8@gmail.com", "ayhamasfoor1@gmail.com", message.as_string())

    motion_frame = None


while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    if alarm_mod:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw

        if threshold.sum() > 1000:
            print(threshold.sum())
            alarm_counter += 1

            motion_frame = frame
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        cv2.imshow("Computer Society", threshold)
    else:
        cv2.imshow("Computer Society", frame)

    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()
            threading.Thread(target=send_email).start()

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("T"):
        alarm_mod = not alarm_mod
        alarm_counter = 0

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("t"):
        alarm_mod = not alarm_mod
        alarm_counter = 0

    if key_pressed == ord("q"):
        alarm_mod = False
        break
    if key_pressed == ord("Q"):
        alarm_mod = False
        break

cap.release()
cv2.destroyWindow()
