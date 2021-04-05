from robot import ROBOT
from world import WORLD
import pybullet_data, time
import pybullet as p
import constants as c
import sys


class SIMULATION:
    def __init__(self):
        solutionID = sys.argv[2]
        if sys.argv[1] == "GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def RUN(self):
        for i in range(0, c.sz - 1):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            if sys.argv[1] == "GUI":
                time.sleep(1 / 240)
        self.robot.Save_Values()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
