import launchpad


# Colors for the launchpad mk2 can be rgb. All of the color's brightness' can go from 0 to 63.
# Since 63 * 4 = 254, every 1 r g or b is actually 4 r g or b
# To get a selected color from a color picker onto the launchpad mk2, divide the r, g, and b by 4
def main():
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

    print("No Launchpads detected, press enter to try again")
    input()
    main()


main()
