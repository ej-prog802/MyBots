import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR
class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(i)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            if jointName == "Torso_BackLeg":
                self.motors[jointName] = MOTOR(jointName)
                self.motors[jointName].frequency = self.motors[jointName].frequency / 2
                self.motors[jointName].Prepare_To_Act()
            else:
                self.motors[jointName] = MOTOR(jointName)


    def Act(self, i):
        for joint in self.motors:
            #leg = joint[6:]
            #action = self.sensors[leg].values[i]
            self.motors[joint].Set_Value(self.robot, i)

    def Save_Values(self):
        for linkName in pyrosim.linkNamesToIndices:
            numpy.save("Data/"+linkName+".npy", self.sensors[linkName].values)
        for jointName in pyrosim.jointNamesToIndices:
            numpy.save("Data/" + jointName + ".npy", self.motors[jointName].motorValues)