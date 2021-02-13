import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
i = .5
while(i<10.5):
    pyrosim.Send_Cube(name="Box", pos=[0, 0, i], size=[length, width, height])
    i += 1
pyrosim.End()