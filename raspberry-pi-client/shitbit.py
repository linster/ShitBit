import RPi.GPIO as GPIO
from firebase import firebase
import time

inputPort = 1

#Setup Firebase
firebase = firebase.FirebaseApplication('https://shitbit-b01de.firebaseio.com/', None)
#Set up GPIO
GPIO.setup(inputPort, GPIO.IN, pull_up_down=GPIO.PUD_UP)

wasTure = False

#Start client
while True:
	if GPIO.input(inputPort):
		print('Input was HIGH')
		if wasTrue == False:
		    print('Input was HIGH')
			post = firebase.post('/', {'time': int(time.time())})
			wasTrue = True
	else:
		if wasTrue == True:
			wasTrue = False
	    print('Input was LOW')
	time.sleep(0.1)
