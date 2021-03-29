import random
import os
import numpy as np
import pyrosim.pyrosim as pyrosim


class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2) * 2 - 1
        self.fitness = None

    def Evaluate(self, show):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        if show:
            os.system("python3 simulate.py GUI")
        else:
            os.system("python3 simulate.py DIRECT")
        self.fitness = float(open('fitness.txt', 'r').read())

    @staticmethod
    def Create_World():
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        pyrosim.Send_Cube(name="Box", pos=[0, 10, height / 2], size=[length, width, height])
        pyrosim.End()

    @staticmethod
    def Generate_Body():
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="0.5 0 1")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="-0.5 0 1")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0, 2)
        col = random.randint(0, 1)
        self.weights[row][col] = random.random() * 2 - 1
