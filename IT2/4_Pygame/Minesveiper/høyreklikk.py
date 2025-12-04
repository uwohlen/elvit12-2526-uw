# Source - https://codereview.stackexchange.com/q
# Posted by George Vasiliou, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-03, License - CC BY-SA 3.0

from evdev import InputDevice
import time
from pymouse import PyMouse
from threading import Timer
import subprocess


def rightclick():
    print "Right Click Timer Starting. Pressed Flag=", pressed
    timestop = time.time()
    endx, endy = m.position()  # Get the coordinates after time has elapsed
    deltatime = timestop - timestart
    if pressed == True and (abs(endx - startx) < 20) and (abs(endy - starty) < 20):
        print 'Timer Finished - Right Click to be injected. Pressed Flag:', pressed, 'Deltatime=', deltatime, ' Delta X:', abs(endx - startx), ' Delta Y:', abs(endy - starty)
    subprocess.check_call(['xinput', '--disable', 'ELAN Touchscreen'])
    m.press(endx, endy, 2)
    m.release(endx, endy, 2)
    subprocess.check_call(['xinput', '--enable', 'ELAN Touchscreen'])

dev = InputDevice('/dev/input/event10')  
# Run evtest to verify the correct ELAN event number and modify above line accordingly
print(dev)  # Print device information
m = PyMouse() #Register a pymouse object

# -------- Right Click Injection without finger relase (Code Begin)

pressed = False
for event in dev.read_loop():
    if event.type == 1 and event.code == 330 and event.value == 1: 
    #corresponds to BTN_TOUCH (330) event. value 1 means btn pressed down = screen pressed
        startx, starty = m.position()  
        # gets mouse current/starting position coordinates
        pressed = True
        timestart = time.time()
        t = Timer(1.0, rightclick) #register a timer of 1 second and call rightclick function when finished.
        t.start() # start the timer

    if event.type == 1 and event.code == 330 and event.value == 0: 
    #corresponds to BTN_TOUCH (330) up event. value 0 means btn up = screen not pressed = finger removed
    # Detecting finger release BTN_TOUCH (330); Value becomes 0.
        print "Finger removed ..."
        pressed = False
        t.cancel() #Cancel the timer and cancel right click injection if finger removed before 1 second (short press , equal to left click on touchscreens)

    if event.type == 3 and event.code == 47 and event.value == 1: 
    #Event ABS_MT_SLOT . This event gets value 1 when 2 fingers touch the screen.
    # Two fingers tap brings right click menu. 
        print "Two Finger tap..."
        x2, y2 = m.position()  # Get the pointer coordinates
        m.click(x2, y2, 2)
        print "Two Finger tap Right Click Injected..."

# --------  Right Click Injection without finger relase (Code End)
