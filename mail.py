import smtplib
import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

myEmail = "rpdb585@gmail.com"
password = "Cabbage1!"

def sendEmail(image):
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = "Doorbell Pushed"
	msgRoot['From'] = myEmail
	msgRoot['To'] = myEmail
	msgRoot.preamble = datetime.datetime.now()
	
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgText = MIMEText('Smart security cam found object')
	msgAlternative.attach(msgText)
	
	msgText = MIMEText('<img src="cidd:image1">','html')
	msgAlternative.attach(msgText)
	
	msgImage = MIMEImage(image)
	msgImage.add_header('Content-ID','<image1>')
	msgRoot.attach(msgImage)
	
	smtp = smtplib.SMTP('smtp.gmail.com',587)
	smtp.starttls()
	smtp.login(myEmail,password)
	smtp.sendEmail(myEmail,myEmail,msgRoot.as_string())
	smtp.quit()
	