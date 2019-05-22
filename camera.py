from picamera import PiCamera
from time import sleep

def pic()
	camera = PiCamera()
	camera.start_preview()
	sleep(2.5)
	camera.capture('/home/i/Desktop/image.jpg')
	camera.stop_preview()