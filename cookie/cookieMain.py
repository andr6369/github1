import P3picam
import picamera
import RPi.GPIO as io
import time

io.setmode(io.BCM)
io.setup(16, io.OUT)

motionState = False

while True:
    motionState = P3picam.motion()
    print(motionState)

    if motionState:
        io.output(16,1)
        time.sleep(0.1)
    
        
    else:
        print("Ingen aktivitet")
        io.output(16,0)
        time.sleep(0.1)
        
