import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    length = 1
    width = 1
    height = 1
    pyrosim.Send_Cube(name="Box", pos=[0, 10, height/2], size=[length, width, height])
    pyrosim.End()
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_Leg", parent="Torso", child="Leg", type="revolute", position="0.5 0 1")
    pyrosim.Send_Cube(name="Leg", pos=[0.5, 0, 0.5], size=[length, width, height])
    pyrosim.End()
Create_World()
Create_Robot()