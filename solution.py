import random
import os
import time
import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim


class SOLUTION:
    def __init__(self, id1):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.fitness = None
        self.myID = id1

    def Evaluate(self, show):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        directOrGUI = "DIRECT "
        if show:
            directOrGUI = "GUI "
        os.system("python3 simulate.py " + directOrGUI + str(self.myID) + " 2&>1 &")

    def Start_Simulation(self, show):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        directOrGUI = "DIRECT "
        if show:
            directOrGUI = "GUI "
        os.system("python3 simulate.py " + directOrGUI + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = 'fitness' + str(self.myID) + '.txt'
        while not os.path.exists(fitnessFileName):
            time.sleep(0.001)
        try:
            self.fitness = float(open(fitnessFileName, 'r').read())
        except:
            self.fitness = 0
        os.system('rm '+fitnessFileName)


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
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="0 0.5 1",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="0 -0.5 1",
                           jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position="0.5 0 1",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position="-0.5 0 1",
                           jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="FrontLeg_FrontFoot", parent="FrontLeg", child="FrontFoot", type="revolute",
                           position="0 1 0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontFoot", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_BackFoot", parent="BackLeg", child="BackFoot", type="revolute",
                           position="0 -1 0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackFoot", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_RightFoot", parent="RightLeg", child="RightFoot", type="revolute",
                           position="-1 0 0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightFoot", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LeftFoot", parent="LeftLeg", child="LeftFoot", type="revolute",
                           position="1 0 0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftFoot", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontFoot")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackFoot")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="RightFoot")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="LeftFoot")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_FrontFoot")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_BackFoot")
        pyrosim.Send_Motor_Neuron(name=15, jointName="RightLeg_RightFoot")
        pyrosim.Send_Motor_Neuron(name=16, jointName="LeftLeg_LeftFoot")
        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        row = random.randint(0, c.numSensorNeurons-1)
        col = random.randint(0, c.numMotorNeurons-1)
        self.weights[row][col] = random.random() * 2 - 1
