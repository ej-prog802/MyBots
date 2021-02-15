import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
z = 0
while(z<6):
    x = 0
    while(x<6):
        y = .5
        length = 1
        width = 1
        height = 1
        while (y < 10.5):
            pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
            y += 1
            length = length * 0.9
            height = height * 0.9
            width = width * 0.9
        x += 1
    z += 1
pyrosim.End()