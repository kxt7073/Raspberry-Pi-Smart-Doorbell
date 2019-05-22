from mail import sendEmail
from camera import pic

def main():
    print("nihaody")
    pic()
    print("swamp")
    sendEmail('/home/pi/Desktop/image.jpg')
    print("hi")
    
if __name__=="__main__":
    main()
