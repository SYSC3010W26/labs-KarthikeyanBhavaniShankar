from picamera2 import Picamera2
import time

def get_camera():
    camera = Picamera2()
    camera.configure(camera.create_still_configuration())
    camera.start()
    return camera

def capture_image(camera, image_out_location, countdown_time=0, preview=False):
    if countdown_time > 0:
        for i in range(countdown_time, 0, -1):
            print(f"Capturing image in {i}...")
            time.sleep(1)

    camera.capture_file(image_out_location)
