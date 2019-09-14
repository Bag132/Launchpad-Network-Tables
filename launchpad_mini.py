import sys
import threading
import logging
from button import Button
from time import sleep
from networktables import NetworkTables

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        print("Import Error")
        sys.exit(-42)

ip = "10.1.25.2"
lp = launchpad.Launchpad()
lp.Open(0, "Launchpad Mini")

forceback = Button(2, 8, 3, 0, name="Force Back")
forcefront = Button(4, 8, 3, 0, name="Force Front")
zero = Button(3, 4, 0, 3, name="Zero")
lowrocket = Button(5, 7, 0, 3, name="Low Rocket")
midrocket = Button(5, 5, 0, 3, name="Mid Rocket")
csfront = Button(7, 5, 0, 3, name="Cargo Ship Front")
csback = Button(0, 5, 0, 3, name="Cargo Ship Back")
highrocket = Button(5, 3, 0, 3, name="High Rocket")
dunk = Button(6, 3, 0, 3, name="Dunk")
groundintake = Button(1, 8, 0, 3, name="Ground Intake")
backpscargointake = Button(0, 1, 0, 3, name="Back PS Cargo Intake")
backpshatchintake = Button(1, 1, 0, 3, name="Back PS Hatch Intake")
frontpshatchintake = Button(7, 1, 0, 3, name="Front PS Hatch Intake")
frontpscargointake = Button(6, 1, 0, 3, name="Front PS Cargo Intake")

buttondict = {
    str(forceback.getx()) + "," + str(forceback.gety()): forceback.getname(),
    str(forcefront.getx()) + "," + str(forcefront.gety()): forcefront.getname(),
    str(zero.getx()) + "," + str(zero.gety()): zero.getname(),
    str(lowrocket.getx()) + "," + str(lowrocket.gety()): lowrocket.getname(),
    str(midrocket.getx()) + "," + str(midrocket.gety()): midrocket.getname(),
    str(csfront.getx()) + "," + str(csfront.gety()): csfront.getname(),
    str(csback.getx()) + "," + str(csback.gety()): csback.getname(),
    str(highrocket.getx()) + "," + str(highrocket.gety()): highrocket.getname(),
    str(dunk.getx()) + "," + str(dunk.gety()): dunk.getname(),
    str(groundintake.getx()) + "," + str(groundintake.gety()): groundintake.getname(),
    str(backpscargointake.getx()) + "," + str(backpscargointake.gety()): backpscargointake.getname(),
    str(backpshatchintake.getx()) + "," + str(backpshatchintake.gety()): backpshatchintake.getname(),
    str(frontpshatchintake.getx()) + "," + str(frontpshatchintake.gety()): frontpshatchintake.getname(),
    str(frontpscargointake.getx()) + "," + str(frontpscargointake.gety()): frontpscargointake.getname()
}

rbaseleft = Button(2, 8, 3, 0)
rbasemiddle = Button(3, 8, 3, 0)
rbaseright = Button(4, 8, 3, 0)
rbasepivot = Button(3, 7, 3, 0)
rbasearm = Button(3, 6, 3, 0)
rbaseee = Button(3, 5, 3, 0)

robotdict = {
    str(rbaseleft.getx()) + "," + str(rbaseleft.gety()): rbaseleft.getname(),
    str(rbasemiddle.getx()) + "," + str(rbasemiddle.gety()): rbasemiddle.getname(),
    str(rbaseright.getx()) + "," + str(rbaseright.gety()): rbaseright.getname(),
    str(rbasepivot.getx()) + "," + str(rbasepivot.gety()): rbasepivot.getname(),
    str(rbasearm.getx()) + "," + str(rbasearm.gety()): rbasearm.getname(),
    str(rbaseee.getx()) + "," + str(rbaseee.gety()): rbaseee.getname()
}

rahead = Button(0, 3, 3, 3)
raheadtop = Button(-1, 2, 3, 3)
raheadbottom = Button(-1, 4, 3, 3)
raheadcenter = Button(-1, 3, 3, 3)
ratrunk1 = Button(-2, 3, 3, 3)
ratrunk2 = Button(-3, 3, 3, 3)
ratrunk3 = Button(-4, 3, 3, 3)
rightarrow = [rahead, raheadbottom, raheadtop, raheadcenter, ratrunk1, ratrunk2, ratrunk3]

rightline = [Button(0, 2, 3, 3), Button(-1, 2, 3, 3)]
leftline = [Button(8, 2, 3, 3), Button(9, 2, 3, 3)]


def fratarget():
    interval = 0.00005
    for i in range(15):
        for j in rightline:
            holdbutton(j.getx() + i, j.gety(), interval)
        sleep(interval)


def flatarget():
    interval = 0.00005

    for i in range(15):
        for j in leftline:
            holdbutton(j.getx() - i, j.gety(), interval)

    sleep(interval)



def flyingrightarrow():
    x = threading.Thread(target=fratarget, daemon=False)
    x.start()


def flyingleftarrow():
    x = threading.Thread(target=flatarget, daemon=False)
    x.start()


# Starts a while loop that displays NUTRONs sliding to the right
def displaynutrons():
    while 1:
        lp.LedCtrlString('NUTRONs ', 3, 0, direction=lp.SCROLL_LEFT, waitms=1)
        sleep(1)


def holdbuttontarget(x, y, time):
    lp.LedCtrlXY(x, y, 3, 3)
    sleep(time)
    lp.LedCtrlXY(x, y, 0, 0)

    if str(x) + "," + str(y) in robotdict:
        lp.LedCtrlXY(x, y, 3, 0)
    elif str(x) + "," + str(y) in buttondict:
        lp.LedCtrlXY(x, y, 0, 3)


def holdbutton(x, y, time):
    x = threading.Thread(target=holdbuttontarget, args=(x, y, time), daemon=False)
    x.start()
    return x


def holdbuttonfadetarget(x, y, time):
    fade = time / 5
    lp.LedCtrlXY(x, y, 1, 1)
    sleep(fade)
    lp.LedCtrlXY(x, y, 2, 2)
    sleep(fade)
    lp.LedCtrlXY(x, y, 3, 3)
    sleep(fade)
    lp.LedCtrlXY(x, y, 2, 2)
    sleep(fade)
    lp.LedCtrlXY(x, y, 1, 1)
    sleep(fade)
    lp.LedCtrlXY(x, y, 0, 0)

    if str(x) + "," + str(y) in robotdict:
        lp.LedCtrlXY(x, y, 3, 0)
    elif str(x) + "," + str(y) in buttondict:
        lp.LedCtrlXY(x, y, 0, 3)


def glowbuttonsincontact(centerx, centery):
    from button import Button
    contactbuttons = []
    b = Button(centerx, centery, 0, 0)

    for i in contactbuttons:
        lp.LedCtrlXY(i.getx(), i.gety(), 0, 3)
    del contactbuttons


def holdbuttonfade(x, y, time):
    x = threading.Thread(target=holdbuttonfadetarget, args=(x, y, time), daemon=False)
    x.start()


def spiraltarget(x, y):
    time = 0.2
    holdbuttonfade(x, y - 1, time - 0.175)

    holdbuttonfade(x + 1, y - 1, time)

    holdbuttonfade(x + 1, y, time)

    holdbuttonfade(x + 1, y + 1, time)

    holdbuttonfade(x, y + 1, time)

    holdbuttonfade(x - 1, y + 1, time)

    holdbuttonfade(x - 1, y, time)

    holdbuttonfade(x - 1, y - 1, time)

    holdbuttonfade(x, y - 1, time)


#     Check if the button is red or not


def spiralaroundbutton(x, y):
    x = threading.Thread(target=spiraltarget, args=(x, y), daemon=False)
    x.start()


def start():
    from button import Button
    lp.Open(0, "Launchpad Mini")
    lp.ButtonFlush()
    lp.Reset()
    logging.basicConfig(level=logging.INFO)
    NetworkTables.initialize("10.1.25.2")
    print("Connecting...")
    while not NetworkTables.isConnected():
        NetworkTables.initialize("10.1.25.2")
        sleep(1)
    table = NetworkTables.getTable("Launchpad")
    print("CONNECTED")

    # lp.LedCtrlString("Rob 195  ", 0, 3, direction=lp.SCROLL_LEFT, waitms=1)
    lp.ButtonFlush()
    try:
        print("READY TO CONTROL")
        # Make base
        lp.LedCtrlXY(2, 8, 3, 0)  # Force back
        lp.LedCtrlXY(3, 8, 3, 0)
        lp.LedCtrlXY(4, 8, 3, 0)  # Force front
        # Make arm
        lp.LedCtrlXY(3, 7, 3, 0)  # Pivot
        lp.LedCtrlXY(3, 6, 3, 0)  # Arm
        lp.LedCtrlXY(3, 5, 3, 0)  # End effector
        # Make score points
        lp.LedCtrlXY(3, 4, 0, 3)  # Zero
        lp.LedCtrlXY(5, 7, 0, 3)  # Low rocket
        lp.LedCtrlXY(5, 5, 0, 3)  # Mid rocket
        lp.LedCtrlXY(7, 5, 0, 3)  # Cargo Ship Front
        lp.LedCtrlXY(0, 5, 0, 3)  # Cargo Ship Back
        lp.LedCtrlXY(5, 3, 0, 3)  # High rocket
        lp.LedCtrlXY(6, 3, 0, 3)  # Dunk
        # Make intake points
        lp.LedCtrlXY(1, 8, 0, 3)  # Ground intake
        lp.LedCtrlXY(0, 1, 0, 3)  # Back Player station cargo intake
        lp.LedCtrlXY(1, 1, 0, 3)  # Back Player station hatch intake
        lp.LedCtrlXY(7, 1, 0, 3)  # Front player station hatch intake
        lp.LedCtrlXY(6, 1, 0, 3)  # Front player station cargo intake

        lp.ButtonFlush()
        limit = lambda n, mini, maxi: max(min(maxi, n), mini)
        # Have methods spiral on and sprial off
        # Start another thread to keep the button spiral on until it sees that button spiral was turned off
        while 1:
            button = lp.ButtonStateXY()
            if button:
                # print("Pressed button: {}:{}:{}".format(button[0], button[1], bool(button[2])))
                butcoords = str(button[0]) + "," + str(button[1])

                if bool(button[2]):
                    spiralaroundbutton(button[0], button[1])

                if button[0] == 4 and button[1] == 8:
                    flyingrightarrow()
                if button[0] == 2 and button[1] == 8:
                    flyingleftarrow()
                if butcoords in buttondict:
                    print("Key: ", buttondict[butcoords])
                    print("Value: ", butcoords)
                    table.putBoolean(buttondict[butcoords], butcoords)

    except AttributeError as a:
        print(a.strerror)
    except Exception as e:
        print(e.strerror)
    finally:
        try:
            lp.Reset()
            lp.Close()
            print("Bruh I though you liked this program smh")
        except AttributeError:
            print(end='')


start()
