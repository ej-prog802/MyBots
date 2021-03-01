
import pybullet as p
import pybullet_data, time, os, numpy
import pyrosim.pyrosim as pyrosim
import random

os.system("python3 generate.py")
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
sz = 1000
backLegSensorValues = numpy.zeros(sz)
frontLegSensorValues = numpy.zeros(sz)
backLegMotorValues = numpy.zeros(sz)
frontLegMotorValues = numpy.zeros(sz)
amplitude = numpy.pi/4
frequency = 50
phaseOffset = 0
targetAngles = numpy.sin(numpy.linspace(-numpy.pi/4, numpy.pi/4, sz))
print(targetAngles)
for i in range(0, sz-1):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex= robot,
        jointName="Torso_BackLeg",
        controlMode= p.POSITION_CONTROL,
        targetPosition= amplitude * numpy.sin(frequency * targetAngles[i] + phaseOffset),
        maxForce= 100)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition= amplitude * numpy.sin(frequency * targetAngles[i] + 1),
        maxForce= 100)
    backLegMotorValues[i] = amplitude * numpy.sin(frequency * targetAngles[i] + phaseOffset)
    frontLegMotorValues[i] = amplitude * numpy.sin(frequency * targetAngles[i] + (numpy.pi))
    time.sleep(1/240)
numpy.save("Data/BackLeg.npy", backLegSensorValues)
numpy.save("Data/FrontLeg.npy", frontLegSensorValues)
numpy.save("Data/BackMotor.npy", backLegMotorValues)
numpy.save("Data/FrontMotor.npy", frontLegMotorValues)
p.disconnect()