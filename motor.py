import numpy
import constants as c
from pyrosim import pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = self.amplitude * numpy.sin(numpy.linspace(-numpy.pi * self.frequency + self.offset,
                                                                     numpy.pi * self.frequency + self.offset, c.sz))

    def Set_Value(self, robot, i):
        #act = 0
        #if i > 0:
        #    act = int(len(self.motorValues)/2)
        targetLocation = self.motorValues[i]
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=targetLocation,
            maxForce=250)
