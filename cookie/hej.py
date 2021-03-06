from Tkinter import *
import tkFont
import picamera
import P3picam
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
GPIO.setup (16,GPIO.OUT)

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

motionState = False

def ledON():
	print("LED button pressed")
	GPIO.output(16,1)
 	while True:
            motionState = P3picam.motion()
            print(motionState)
            ledButton["text"] = "LED ON"
            
	else:
		GPIO.output(16,GPIO.HIGH)
                ledButton["text"] = "LED OFF"

def exitProgram():
	print("Exit Button pressed")
        GPIO.cleanup()
	win.quit()


win.title("First GUI")
win.geometry('800x480')

exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

ledButton = Button(win, text = "LED ON", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack()




mainloop()
