import constants as c
import numpy
from pyrosim import pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.values = numpy.zeros(c.sz-1)
        self.linkName = linkName

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

