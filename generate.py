import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    length = 1
    width = 1
    height = 1
    pyrosim.Send_Cube(name="Box", pos=[0, 0, height/2], size=[length, width, height])
    pyrosim.End()