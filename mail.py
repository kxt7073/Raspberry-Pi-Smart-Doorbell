import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

myEmail = "Your email"
password = "Your password"

def sendEmail(image):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = "Doorbell Pushed"
    msgRoot['From'] = myEmail
    msgRoot['To'] = myEmail
    msgRoot.preamble = "test "
    
    #msgAlternative = MIMEMultipart('alternative')
    #msgRoot.attach(msgAlternative)
    #msgText = MIMEText('Smart security cam found object')
    #msgAlternative.attach(msgText)
    
    #msgText = MIMEText('<img src="cidd:image1">','html')
    #msgAlternative.attach(msgText)
    
    img = open(image,'rb').read()
    image = MIMEImage(img,name=os.path.basename(image))
    msgRoot.attach(image)
    
    #msgImage = MIMEImage(image)
    #msgImage.add_header('Content-ID','<image1>')
    #msgRoot.attach(msgImage)
    
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    #smtp.ehlo()
    smtp.starttls()
    #smtp.ehlo()
    smtp.login(myEmail,password)
    
    smtp.sendmail(myEmail,myEmail,msgRoot.as_string())
    smtp.quit()
    