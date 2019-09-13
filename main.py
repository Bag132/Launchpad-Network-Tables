import sys
from networktables import NetworkTables

import logging

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        print("Import Error")
        sys.exit(-42)

lp = launchpad.Launchpad()

if lp.Open(0, "Launchpad Mini"):
    print("Detected Launchpad")
else:
    print("No Launchpads detected...")
    print("Deleting file(s) \"C:\\Windows\\System32\"")
    sys.exit(-32)

lp.ButtonFlush()
lp.Reset()
NetworkTables.initialize("10.1.25.2")
table = NetworkTables.getTable("Launchpad")
started = True
print("CONNECTED")
lp.LedCtrlString("Rob 195  ", 0, 3, waitms=1)
lp.ButtonFlush()

try:
    print("All systems go")
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

    while 1:
        button = lp.ButtonStateXY()
        if button:
            x = int(button[0]) + 1
            y = int(button[1])
            status = "off"
            if bool(button[2]):
                status = "on"

            print("Pressed button: {}:{}:{}".format(x, y, status))

            table.putBoolean("{},{}".format(x, y), button[2])

except AttributeError:
    print("Boodgye")
except Exception as e:
    print(str(e))
finally:
    try:
        lp.Reset()
        lp.Close()
        print("Bruh I though you liked this program smh")
    except AttributeError:
        print(end='')
