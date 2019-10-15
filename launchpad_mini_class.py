import sys
import threading
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


class LaunchpadRunner:

    def __init__(self, lp, buttons):
        self.lp = lp
        self.buttons = buttons
        self.rbaseleft = Button(lp, 2, 8, 3, 0)
        self.rbasemiddle = Button(lp, 3, 8, 3, 0)
        self.rbaseright = Button(lp, 4, 8, 3, 0)
        self.rbasepivot = Button(lp, 3, 7, 3, 0)
        self.rbasearm = Button(lp, 3, 6, 3, 0)
        self.rbaseee = Button(lp, 3, 5, 3, 0)
        self.rahead = Button(lp, 0, 3, 3, 3)
        self.raheadtop = Button(lp, -1, 2, 3, 3)
        self.raheadbottom = Button(lp, -1, 4, 3, 3)
        self.raheadcenter = Button(lp, -1, 3, 3, 3)
        self.ratrunk1 = Button(lp, -2, 3, 3, 3)
        self.ratrunk2 = Button(lp, -3, 3, 3, 3)
        self.ratrunk3 = Button(lp, -4, 3, 3, 3)
        self.rightarrow = [self.rahead, self.raheadbottom, self.raheadtop, self.raheadcenter, self.ratrunk1, self.ratrunk2, self.ratrunk3]

        self.lahead = Button(lp, 8, 3, 3, 3)
        self.laheadtop = Button(lp, 9, 2, 3, 3)
        self.laheadbottom = Button(lp, 9, 4, 3, 3)
        self.laheadcenter = Button(lp, 9, 3, 3, 3)
        self.latrunk1 = Button(lp, 10, 3, 3, 3)
        self.latrunk2 = Button(lp, 11, 3, 3, 3)
        self.latrunk3 = Button(lp, 12, 3, 3, 3)
        self.leftarrow = [self.lahead, self.laheadbottom, self.laheadtop, self.laheadcenter, self.latrunk1, self.latrunk2, self.latrunk3]

        self.rightline = [Button(lp, 0, 2, 3, 3), Button(lp, -1, 2, 3, 3)]
        self.leftline = [Button(lp, 8, 2, 3, 3), Button(lp, 9, 2, 3, 3)]

        self.buttondict = {}
        for b in buttons:
            self.buttondict.update()

    def start(self):
        pass

    def fratarget(self):
        interval = 0
        for i in range(15):
            self.lp.LedCtrlXY(self.rahead.getx() + i, self.rahead.gety(), 3, 3)
            self.lp.LedCtrlXY(self.raheadtop.getx() + i, self.raheadtop.gety(), 3, 3)
            self.lp.LedCtrlXY(self.raheadbottom.getx() + i, self.raheadbottom.gety(), 3, 3)
            self.lp.LedCtrlXY(self.raheadcenter.getx() + i, self.raheadcenter.gety(), 3, 3)
            self.lp.LedCtrlXY(self.ratrunk1.getx() + i, self.ratrunk1.gety(), 3, 3)
            self.lp.LedCtrlXY(self.ratrunk2.getx() + i, self.ratrunk2.gety(), 3, 3)
            self.lp.LedCtrlXY(self.ratrunk3.getx() + i, self.ratrunk3.gety(), 3, 3)
            sleep(interval)
            if str(self.rahead.getx() + i) + "," + str(self.rahead.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.rahead.getx() + i, self.rahead.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.rahead.getx() + i, self.rahead.gety(), 0, 0)
            if str(self.raheadtop.getx() + i) + "," + str(self.raheadtop.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.raheadtop.getx() + i, self.raheadtop.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.raheadtop.getx() + i, self.raheadtop.gety(), 0, 0)
            if str(self.raheadbottom.getx() + i) + "," + str(self.raheadbottom.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.raheadbottom.getx() + i, self.raheadbottom.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.raheadbottom.getx() + i, self.raheadbottom.gety(), 0, 0)
            if str(self.raheadcenter.getx() + i) + "," + str(self.raheadcenter.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.raheadcenter.getx() + i, self.raheadcenter.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.raheadcenter.getx() + i, self.raheadcenter.gety(), 0, 0)
            if str(self.ratrunk1.getx() + i) + "," + str(self.ratrunk1.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.ratrunk1.getx() + i, self.ratrunk1.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.ratrunk1.getx() + i, self.ratrunk1.gety(), 0, 0)
            if str(self.ratrunk2.getx() + i) + "," + str(self.ratrunk2.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.ratrunk2.getx() + i, self.ratrunk2.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.ratrunk2.getx() + i, self.ratrunk2.gety(), 0, 0)
            if str(self.ratrunk3.getx() + i) + "," + str(self.ratrunk3.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.ratrunk3.getx() + i, self.ratrunk3.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.ratrunk3.getx() + i, self.ratrunk3.gety(), 0, 0)

    def flatarget(self):
        interval = 0

        for i in range(15):
            self.lp.LedCtrlXY(self.lahead.getx() - i, self.lahead.gety(), 3, 3)
            self.lp.LedCtrlXY(self.laheadtop.getx() - i, self.laheadtop.gety(), 3, 3)
            self.lp.LedCtrlXY(self.laheadbottom.getx() - i, self.laheadbottom.gety(), 3, 3)
            self.lp.LedCtrlXY(self.laheadcenter.getx() - i, self.laheadcenter.gety(), 3, 3)
            self.lp.LedCtrlXY(self.latrunk1.getx() - i, self.latrunk1.gety(), 3, 3)
            self.lp.LedCtrlXY(self.latrunk2.getx() - i, self.latrunk2.gety(), 3, 3)
            self.lp.LedCtrlXY(self.latrunk3.getx() - i, self.latrunk3.gety(), 3, 3)
            sleep(interval)
            if str(self.lahead.getx() - i) + "," + str(self.lahead.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.lahead.getx() - i, self.lahead.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.lahead.getx() - i, self.lahead.gety(), 0, 0)
            if str(self.laheadtop.getx() - i) + "," + str(self.laheadtop.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.laheadtop.getx() - i, self.laheadtop.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.laheadtop.getx() - i, self.laheadtop.gety(), 0, 0)
            if str(self.laheadbottom.getx() - i) + "," + str(self.laheadbottom.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.laheadbottom.getx() - i, self.laheadbottom.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.laheadbottom.getx() - i, self.laheadbottom.gety(), 0, 0)
            if str(self.laheadcenter.getx() - i) + "," + str(self.laheadcenter.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.laheadcenter.getx() - i, self.laheadcenter.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.laheadcenter.getx() - i, self.laheadcenter.gety(), 0, 0)
            if str(self.latrunk1.getx() - i) + "," + str(self.latrunk1.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.latrunk1.getx() - i, self.latrunk1.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.latrunk1.getx() - i, self.latrunk1.gety(), 0, 0)
            if str(self.latrunk2.getx() - i) + "," + str(self.latrunk2.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.latrunk2.getx() - i, self.latrunk2.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.latrunk2.getx() - i, self.latrunk2.gety(), 0, 0)
            if str(self.latrunk3.getx() - i) + "," + str(self.latrunk3.gety()) in self.buttondict:
                self.lp.LedCtrlXY(self.latrunk3.getx() - i, self.latrunk3.gety(), 0, 3)
            else:
                self.lp.LedCtrlXY(self.latrunk3.getx() - i, self.latrunk3.gety(), 0, 0)

    def flyingrightarrow(self):
        x = threading.Thread(target=self.fratarget, daemon=False)
        x.start()

    def flyingleftarrow(self):
        x = threading.Thread(target=self.flatarget, daemon=False)
        x.start()

    # Starts a while loop that displays NUTRONs sliding to the right
    def displaynutrons(self):
        while 1:
            self.lp.LedCtrlString('NUTRONs ', 3, 0, direction=self.lp.SCROLL_LEFT, waitms=1)
            sleep(1)

    def holdbuttontarget(self, x, y, time):
        self.lp.LedCtrlXY(x, y, 3, 3)
        sleep(time)
        self.lp.LedCtrlXY(x, y, 0, 0)

        if str(x) + "," + str(y) in self.robotdict:
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
