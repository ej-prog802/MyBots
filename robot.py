import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from motor import MOTOR
from sensor import SENSOR
class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain.nndf")
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


    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robot, desiredAngle)

    def Think(self):
        self.nn.Update()

    def Save_Values(self):
        for linkName in pyrosim.linkNamesToIndices:
            numpy.save("Data/"+linkName+".npy", self.sensors[linkName].values)
        for jointName in pyrosim.jointNamesToIndices:
            numpy.save("Data/" + jointName + ".npy", self.motors[jointName].motorValues)