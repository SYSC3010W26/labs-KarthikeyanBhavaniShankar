from helper_functions.camera import get_camera, capture_image
from helper_functions.computer_vision import person_detected
from helper_functions.sensehat import get_sensehat, alarm
import time

BG_IMG = "data/images/background.jpg"
TEST_IMG = "data/images/test.jpg"

camera = get_camera()
sense = get_sensehat()

print("1 - Take background image")
print("2 - Arm system")
choice = input("Enter choice: ")

if choice == "1":
    print("Get out of the scene!")
    capture_image(camera, BG_IMG, countdown_time=10)
    print("Background image saved.")

elif choice == "2":
    interval = int(input("Enter capture interval (seconds): "))
    threshold = int(input("Enter threshold t1: "))
    print("Monitoring starts in 10 seconds...")
    time.sleep(10)

    while True:
        capture_image(camera, TEST_IMG)
        if person_detected(BG_IMG, TEST_IMG, threshold):
            print("🚨 PERSON DETECTED 🚨")
            alarm(sense, 5)
        else:
            print("No person detected")
        time.sleep(interval)
