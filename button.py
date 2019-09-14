import launchpad


class Button:
    buttons = []

    def __init__(self, x, y, red, green, blue=0, name="No Name"):
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
