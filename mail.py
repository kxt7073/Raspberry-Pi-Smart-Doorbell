"""
    Mail program for Smart Raspberry Pi Doorbell
    @author Kevin Ta : kevinduynta@gmail.com
    Date 5/24/2019
"""
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

myEmail = "Your email"
password = "Your password"

#Sends an email notification to desired email
#For this project it emails itself
#If desired to send an email from and to a different person
#Uncomment and add the desired email to send to
#ToEmail = "To person email"
#Also change Line 20 from 'myEmail' to 'ToEmail'
#And change line 31 second instance of 'myEmail' to 'ToEmail'
def sendEmail(image):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = "Doorbell Pushed"
    msgRoot['From'] = myEmail
    msgRoot['To'] = myEmail #ToEmail
    msgRoot.preamble = "test "
        
    img = open(image,'rb').read()
    image = MIMEImage(img,name=os.path.basename(image))
    msgRoot.attach(image)
    
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login(myEmail,password)
    smtp.sendmail(myEmail,myEmail,msgRoot.as_string())
    smtp.quit()
    