"""
    Main program for Smart Raspberry Pi Doorbell
    @author Kevin Ta : kevinduynta@gmail.com
    Date 5/24/2019
"""
from mail import sendEmail
from picamera import PiCamera
from camera import pic
import RPi.GPIO as G

#Setup GPIO board, this project uses GPIO 2,38,39,40
G.setwarnings(False)
G.setmode(G.BOARD)
G.setup(40,G.OUT)
G.setup(38,G.OUT)  

#Waits for doorbell to be pushed and then takes a picture
#and sends said picture to desired email in mail.py
def main():
    camera = PiCamera()
    while True:
        if G.input(40)==G.HIGH:
            G.output(38,G.HIGH)
            pic(camera)
            print("swamp")
            sendEmail('/home/pi/Desktop/image.jpg') 
        else:
            G.output(38,G.LOW)
            
if __name__=="__main__":
    main()
