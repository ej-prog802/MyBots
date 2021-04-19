import numpy
import os
import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from motor import MOTOR
from sensor import SENSOR
import numpy as np
class ROBOT:

    def __init__(self, id1):
        self.sensors = {}
        self.motors = {}
        self.myID = str(id1)
        self.nn = NEURAL_NETWORK("brain"+self.myID+".nndf")
        os.system('rm brain'+self.myID+'.nndf')
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
            self.motors[jointName] = MOTOR(jointName)


    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robot, desiredAngle*c.motorJointRange)

    def Think(self):
        self.nn.Update()

    def Save_Values(self):
        for linkName in pyrosim.linkNamesToIndices:
            numpy.save("Data/"+linkName+".npy", self.sensors[linkName].values)
        for jointName in pyrosim.jointNamesToIndices:
            numpy.save("Data/" + jointName + ".npy", self.motors[jointName].motorValues)

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        yPosition = basePosition[1]
        zPosition = basePosition[2]
        footSense = []
        for i in range(0, c.sz - 1):
            FrontFoot = self.sensors["FrontFoot"].values[i]
            BackFoot = self.sensors["BackFoot"].values[i]
            LeftFoot = self.sensors["LeftFoot"].values[i]
            RightFoot = self.sensors["RightFoot"].values[i]
            footSense.append(numpy.mean([FrontFoot,BackFoot,LeftFoot,RightFoot]))
        offset = numpy.log((numpy.abs(yPosition) + numpy.abs(xPosition)))*c.offWeight
        height = numpy.log(zPosition)*c.heightWeight
        jummpyness = (0-height)+offset
        file = open('fitness'+self.myID+'.txt', 'w')
        file.write(str(jummpyness))
        file.close()
