from robot import ROBOT
from world import WORLD
import pybullet_data, time
import pybullet as p
import constants as c
class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def RUN(self):
        for i in range(0, c.sz - 1):
         p.stepSimulation()
         self.robot.Sense(i)
         self.robot.Think()
         self.robot.Act()
         time.sleep(1/60)
        self.robot.Save_Values()

    def __del__(self):
        p.disconnect()