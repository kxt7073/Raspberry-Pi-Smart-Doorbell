from picamera import PiCamera
from time import sleep

def pic():
    camera = PiCamera()
    camera.start_preview()
    sleep(2.5)
    picture = camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    return picture
    
if __name__ == "__main__":
    pic()