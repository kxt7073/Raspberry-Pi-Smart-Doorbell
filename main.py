import mail
import camera

def main():
	picture = camera.pic()
	mail.sendEmail(picture)
	