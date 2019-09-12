import sys
import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging

sd = NetworkTables.getTable("SmartDashboard")

i = 0


# while True:
#     print("robotTime:", sd.getNumber("robotTime", "N/A"))
#
#     sd.putNumber("dsTime", i)
#     time.sleep(1)
#     i += 1

class NetworkTable:
    def __init__(self, ip):
        logging.basicConfig(level=logging.DEBUG)
        NetworkTables.initialize(server=ip)

    def start(self):
        table = NetworkTables.getTable("")