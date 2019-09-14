import launchpad

lp = launchpad.Launchpad()

if lp.Check(0, "mk2"):
    lp = launchpad.LaunchpadMk2()
    if lp.Open(0, "Launchpad Mk2"):
        print("Detected Launchpad Mk2")

else:
    if lp.Open(0, "Launchpad Mini"):
        print("Detected Launchpad Mini")
        import launchpad_mini
        launchpad_mini.start(lp)

