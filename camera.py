"""
    Camera program for Smart Raspberry Pi Doorbell
    @author Kevin Ta : kevinduynta@gmail.com
    Date 5/24/2019
"""
from picamera import PiCamera
from time import sleep

#Captures a picture and saves as image.jpg
def pic(camera):
    camera.start_preview()
    sleep(2.5)
    picture = camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    
if __name__ == "__main__":
    pic()