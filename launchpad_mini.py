import sys
import threading
# import logging
# from concurrent.futures.thread import ThreadPoolExecutor

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

columnsused = -1

forceback = Button(2, 8, 3, 0, name="Force Back")
forcefront = Button(4, 8, 3, 0, name="Force Front")
zero = Button(3, 4, 0, 3, name="Zero")
lowrocket = Button(5, 7, 0, 3, name="Low Rocket")
midrocket = Button(5, 5, 0, 3, name="Mid Rocket")
csfront = Button(7, 5, 0, 3, name="Cargo Ship Front")
csback = Button(0, 5, 0, 3, name="Cargo Ship Back")
highrocket = Button(5, 3, 0, 3, name="High Rocket")
dunk = Button(6, 3, 0, 3, name="Dunk")
groundintake = Button(0, 8, 0, 3, name="Ground Intake")
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

lahead = Button(8, 3, 3, 3)
laheadtop = Button(9, 2, 3, 3)
laheadbottom = Button(9, 4, 3, 3)
laheadcenter = Button(9, 3, 3, 3)
latrunk1 = Button(10, 3, 3, 3)
latrunk2 = Button(11, 3, 3, 3)
latrunk3 = Button(12, 3, 3, 3)
leftarrow = [lahead, laheadbottom, laheadtop, laheadcenter, latrunk1, latrunk2, latrunk3]

rightline = [Button(0, 2, 3, 3), Button(-1, 2, 3, 3)]
leftline = [Button(8, 2, 3, 3), Button(9, 2, 3, 3)]


def start(lp):
    stopthreads = False

    def fratarget():
        interval = 0
        for i in range(15):
            lp.LedCtrlXY(rahead.getx() + i, rahead.gety(), 3, 3)
            lp.LedCtrlXY(raheadtop.getx() + i, raheadtop.gety(), 3, 3)
            lp.LedCtrlXY(raheadbottom.getx() + i, raheadbottom.gety(), 3, 3)
            lp.LedCtrlXY(raheadcenter.getx() + i, raheadcenter.gety(), 3, 3)
            lp.LedCtrlXY(ratrunk1.getx() + i, ratrunk1.gety(), 3, 3)
            lp.LedCtrlXY(ratrunk2.getx() + i, ratrunk2.gety(), 3, 3)
            lp.LedCtrlXY(ratrunk3.getx() + i, ratrunk3.gety(), 3, 3)
            sleep(interval)
            if str(rahead.getx() + i) + "," + str(rahead.gety()) in buttondict:
                lp.LedCtrlXY(rahead.getx() + i, rahead.gety(), 0, 3)
            else:
                lp.LedCtrlXY(rahead.getx() + i, rahead.gety(), 0, 0)
            if str(raheadtop.getx() + i) + "," + str(raheadtop.gety()) in buttondict:
                lp.LedCtrlXY(raheadtop.getx() + i, raheadtop.gety(), 0, 3)
            else:
                lp.LedCtrlXY(raheadtop.getx() + i, raheadtop.gety(), 0, 0)
            if str(raheadbottom.getx() + i) + "," + str(raheadbottom.gety()) in buttondict:
                lp.LedCtrlXY(raheadbottom.getx() + i, raheadbottom.gety(), 0, 3)
            else:
                lp.LedCtrlXY(raheadbottom.getx() + i, raheadbottom.gety(), 0, 0)
            if str(raheadcenter.getx() + i) + "," + str(raheadcenter.gety()) in buttondict:
                lp.LedCtrlXY(raheadcenter.getx() + i, raheadcenter.gety(), 0, 3)
            else:
                lp.LedCtrlXY(raheadcenter.getx() + i, raheadcenter.gety(), 0, 0)
            if str(ratrunk1.getx() + i) + "," + str(ratrunk1.gety()) in buttondict:
                lp.LedCtrlXY(ratrunk1.getx() + i, ratrunk1.gety(), 0, 3)
            else:
                lp.LedCtrlXY(ratrunk1.getx() + i, ratrunk1.gety(), 0, 0)
            if str(ratrunk2.getx() + i) + "," + str(ratrunk2.gety()) in buttondict:
                lp.LedCtrlXY(ratrunk2.getx() + i, ratrunk2.gety(), 0, 3)
            else:
                lp.LedCtrlXY(ratrunk2.getx() + i, ratrunk2.gety(), 0, 0)
            if str(ratrunk3.getx() + i) + "," + str(ratrunk3.gety()) in buttondict:
                lp.LedCtrlXY(ratrunk3.getx() + i, ratrunk3.gety(), 0, 3)
            else:
                lp.LedCtrlXY(ratrunk3.getx() + i, ratrunk3.gety(), 0, 0)

    def flatarget():
        interval = 0

        for i in range(15):
            lp.LedCtrlXY(lahead.getx() - i, lahead.gety(), 3, 3)
            lp.LedCtrlXY(laheadtop.getx() - i, laheadtop.gety(), 3, 3)
            lp.LedCtrlXY(laheadbottom.getx() - i, laheadbottom.gety(), 3, 3)
            lp.LedCtrlXY(laheadcenter.getx() - i, laheadcenter.gety(), 3, 3)
            lp.LedCtrlXY(latrunk1.getx() - i, latrunk1.gety(), 3, 3)
            lp.LedCtrlXY(latrunk2.getx() - i, latrunk2.gety(), 3, 3)
            lp.LedCtrlXY(latrunk3.getx() - i, latrunk3.gety(), 3, 3)
            sleep(interval)
            if str(lahead.getx() - i) + "," + str(lahead.gety()) in buttondict:
                lp.LedCtrlXY(lahead.getx() - i, lahead.gety(), 0, 3)
            else:
                lp.LedCtrlXY(lahead.getx() - i, lahead.gety(), 0, 0)
            if str(laheadtop.getx() - i) + "," + str(laheadtop.gety()) in buttondict:
                lp.LedCtrlXY(laheadtop.getx() - i, laheadtop.gety(), 0, 3)
            else:
                lp.LedCtrlXY(laheadtop.getx() - i, laheadtop.gety(), 0, 0)
            if str(laheadbottom.getx() - i) + "," + str(laheadbottom.gety()) in buttondict:
                lp.LedCtrlXY(laheadbottom.getx() - i, laheadbottom.gety(), 0, 3)
            else:
                lp.LedCtrlXY(laheadbottom.getx() - i, laheadbottom.gety(), 0, 0)
            if str(laheadcenter.getx() - i) + "," + str(laheadcenter.gety()) in buttondict:
                lp.LedCtrlXY(laheadcenter.getx() - i, laheadcenter.gety(), 0, 3)
            else:
                lp.LedCtrlXY(laheadcenter.getx() - i, laheadcenter.gety(), 0, 0)
            if str(latrunk1.getx() - i) + "," + str(latrunk1.gety()) in buttondict:
                lp.LedCtrlXY(latrunk1.getx() - i, latrunk1.gety(), 0, 3)
            else:
                lp.LedCtrlXY(latrunk1.getx() - i, latrunk1.gety(), 0, 0)
            if str(latrunk2.getx() - i) + "," + str(latrunk2.gety()) in buttondict:
                lp.LedCtrlXY(latrunk2.getx() - i, latrunk2.gety(), 0, 3)
            else:
                lp.LedCtrlXY(latrunk2.getx() - i, latrunk2.gety(), 0, 0)
            if str(latrunk3.getx() - i) + "," + str(latrunk3.gety()) in buttondict:
                lp.LedCtrlXY(latrunk3.getx() - i, latrunk3.gety(), 0, 3)
            else:
                lp.LedCtrlXY(latrunk3.getx() - i, latrunk3.gety(), 0, 0)

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

    def holdbuttonnocheck(x, y, time):
        lp.LedCtrlXY(x, y, 3, 3)
        sleep(time)
        lp.LedCtrlXY(x, y, 0, 0)

    def holdbutton(x, y, time, check=True):
        if check:
            t = threading.Thread(target=holdbuttontarget, args=(x, y, time), daemon=False)
        else:
            t = threading.Thread(target=holdbuttonnocheck, args=(x, y, time), daemon=False)
        t.start()
        return t

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

    def spiralaroundbutton(x, y):
        x = threading.Thread(target=spiraltarget, args=(x, y), daemon=False)
        x.start()

    def updownbutton(x):
        interval = 0.1
        y = 4
        goup = True
        godown = False
        while 1 and not stopthreads:
            while goup and not stopthreads:
                holdbutton(x, y, interval, check=False)
                sleep(interval)
                y -= 1
                if y == 0:
                    goup = False
                    godown = True

            while godown and not stopthreads:
                holdbutton(x, y, interval, check=False)
                sleep(interval)
                y += 1
                if y == 8:
                    godown = False
                    goup = True

    def displayconnectingtarget():
        interval = 0.11
        t0 = threading.Thread(target=updownbutton, args=[0], daemon=False)
        t1 = threading.Thread(target=updownbutton, args=[1], daemon=False)
        t2 = threading.Thread(target=updownbutton, args=[2], daemon=False)
        t3 = threading.Thread(target=updownbutton, args=[3], daemon=False)
        t4 = threading.Thread(target=updownbutton, args=[4], daemon=False)
        t5 = threading.Thread(target=updownbutton, args=[5], daemon=False)
        t6 = threading.Thread(target=updownbutton, args=[6], daemon=False)
        t7 = threading.Thread(target=updownbutton, args=[7], daemon=False)
        t8 = threading.Thread(target=updownbutton, args=[8], daemon=False)

        t0.start()
        sleep(interval)
        t1.start()
        sleep(interval)
        t2.start()
        sleep(interval)
        t3.start()
        sleep(interval)
        t4.start()
        sleep(interval)
        t5.start()
        sleep(interval)
        t6.start()
        sleep(interval)
        t7.start()
        sleep(interval)
        t8.start()

        return [t0, t1, t2, t3, t4, t5, t6, t7, t8]

    def displayconnecting():
        x = threading.Thread(target=displayconnectingtarget, daemon=False)
        x.start()
        return x

    try:
        lp.ButtonFlush()
    except AttributeError:
        print("Launchpad may not be plugged in")

    lp.Reset()
    # logging.basicConfig(level=logging.INFO)
    displayconnecting()
    NetworkTables.initialize("10.1.25.2")
    print("Connecting...")
    while not NetworkTables.isConnected():
        NetworkTables.initialize("10.1.25.2")
        sleep(1)
    table = NetworkTables.getTable("Launchpad")
    # sleep(5)
    print("CONNECTED")
    stopthreads = True
    sleep(0.5)
    # lp.LedCtrlString("Rob195 ", 0, 3, direction=lp.SCROLL_LEFT, waitms=0)
    lp.ButtonFlush()

    try:
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
        lp.LedCtrlXY(0, 8, 0, 3)  # Ground intake
        lp.LedCtrlXY(0, 1, 0, 3)  # Back Player station cargo intake
        lp.LedCtrlXY(1, 1, 0, 3)  # Back Player station hatch intake
        lp.LedCtrlXY(7, 1, 0, 3)  # Front player station hatch intake
        lp.LedCtrlXY(6, 1, 0, 3)  # Front player station cargo intake

        lp.ButtonFlush()
        patricklomba = True
        print("READY TO CONTROL")
        while patricklomba:
            button = lp.ButtonStateXY()
            if button:
                print("Pressed button: {}:{}:{}".format(button[0], button[1], bool(button[2])))
                butcoords = str(button[0]) + "," + str(button[1])

                if bool(button[2]):
                    spiralaroundbutton(button[0], button[1])
                if button[0] == 4 and button[1] == 8 and bool(button[2]):
                    flyingrightarrow()
                if button[0] == 2 and button[1] == 8 and bool(button[2]):
                    flyingleftarrow()

                if butcoords in buttondict:
                    print("Key: ", buttondict[butcoords])
                    print("Value: ", butcoords)

                    table.putBoolean(buttondict[butcoords], bool(button[2]))

    except Exception as e:
        print(e)
    finally:
        try:
            lp.Reset()
            lp.Close()
            print("Bruh I though you liked this program smh")
        except AttributeError:
            print(end='')
