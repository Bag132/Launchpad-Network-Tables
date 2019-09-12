import sys

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        print("Import Error")
        sys.exit(-42)

lp = launchpad.Launchpad()


def start():
    try:
        if lp.Open(0, "Launchpad Mini"):
            print("Detected Launchpad")
        else:
            print("No Launchpads detected...")
            print("Deleting file(s) 'C:\\Windows\\System32'")
            sys.exit(-32)

        lp.LedCtrlString("Rob 195  ", 0, 3, waitms=1)
        lp.ButtonFlush()
    except Exception as e:
        print(str(e))
        stop()


def main():
    try:
        print("All systems go")
        while 1:
            button = lp.ButtonStateXY()
            if button:
                x = int(button[0]) + 1
                y = int(button[1])
                status = "off"
                if bool(button[2]):
                    status = "on"

                print("Pressed button: ({}, {}):{}".format(x, y, status))
                if x == 9 and y == 8:
                    break
    except AttributeError:
        print("Boodgye")
    except Exception as e:
        print(str(e))
    finally:
        stop()


def stop():
    try:
        lp.Reset()
        lp.Close()
        print("Bruh I though you liked this program smh")
    except AttributeError:
        print(end='')


def restart():
    while 1:
        if str(input()) == "r":
            stop()
            start()
            main()


start()
main()
stop()
