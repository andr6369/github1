from Tkinter import *
import tkFont
import RPi.GPIO as GPIO
import time
from picamera import PiCamera, Color

camera = PiCamera()

GPIO.setmode (GPIO.BCM)
GPIO.setup (16,GPIO.OUT)

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')


def ledON():
    
    print("Du har trykket")
    
    while True:
        camera.resolution = (2592, 1944)
        camera.framerate = 15
        camera.start_preview()
        camera.annotate_text = "3"
        GPIO.output(16,1)
        time.sleep(2)
        camera.annotate_text = "2"
        time.sleep(2)
        camera.annotate_text = "1"
        camera.image_effect = 'negative'
        time.sleep(2)
        camera.capture('/home/pi/Desktop/image12.jpg')
        camera.stop_preview()
        GPIO.output(16,0)
        break

def exitProgram():
    print("Afsluttet")
    GPIO.cleanup()
    win.quit()
    
    


win.title("First GUI")
win.geometry('1200x680')

exitButton  = Button(win, text = "Slut", font = myFont, command = exitProgram, height =2 , width = 10) 
exitButton.pack(side = BOTTOM)

ledButton = Button(win, text = "Tag billede", font = myFont, command = ledON, height = 2, width =14 )
ledButton.pack(side = TOP)


mainloop()
