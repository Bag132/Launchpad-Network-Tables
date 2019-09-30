# Colors for the launchpad mk2 can be rgb. All of the color's brightness' can go from 0 to 63.
# Since 63 * 4 = 254, every 1 r g or b is actually 4 r g or b
# To get a selected color from a color picker onto the launchpad mk2, divide the r, g, and b by 4

ANSI_RESET = "\u001B[0m"
ANSI_BLACK = "\u001B[30m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
ANSI_CYAN = "\u001B[36m"
ANSI_WHITE = "\u001B[37m"

print(ANSI_YELLOW + "IF ANYTHING STOPS OR DOESN'T WORK, STOP THIS PROGRAM, UNPLUG AND REPLUG THE LAUNCHPAD, THEN START "
                    "THIS PROGRAM AGAIN" + ANSI_PURPLE)


def main():
    import launchpad
    lp = launchpad.Launchpad()
    if lp.Check(0, "mk2"):
        lp = launchpad.LaunchpadMk2()
        if lp.Open(0, "Launchpad Mk2"):
            print("Detected Launchpad Mk2")
        import launchpad_mk2
        launchpad_mk2.start(lp)

    else:
        if lp.Open(0, "Launchpad Mini"):
            print("Detected Launchpad Mini")
            import launchpad_mini
            launchpad_mini.start(lp)

    print(ANSI_RED + "No Launchpads detected, restart program to try again" + ANSI_RESET)


main()
