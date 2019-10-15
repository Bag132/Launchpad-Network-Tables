import launchpad


class Button:
    buttons = []

    def __init__(self, lp, x, y, red, green, blue=0, name="No Name"):
        self.lp = lp
        self.x = x
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue
        self.name = name
        Button.buttons.append(self)

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def setred(self, red):
        self.red = red

    def setgreen(self, green):
        self.green = green

    def setblue(self, blue):
        self.blue = blue

    def setname(self, name):
        self.name = name

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getred(self):
        return self.red

    def getgreen(self):
        return self.green

    def getblue(self):
        return self.blue

    def getname(self):
        return self.name

    def get_launchpad(self):
        return self.lp

    def light_button_up(self):
        if type(self.lp) == launchpad.Launchpad:
            self.lp.LedCtrlXY(self.x, self.y, self.red, self.green)
        elif type(self.lp) == launchpad.LaunchpadMk2 or type(self.lp) == launchpad.Launchpad:
            self.lp.LedCtrlXY(self.x, self.y, self.red, self.green, blue=self.blue)
