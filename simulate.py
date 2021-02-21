import pybullet as p
import pybullet_data, time, os, numpy
import pyrosim.pyrosim as pyrosim
os.system("python3 generate.py")
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(500)
frontLegSensorValues = numpy.zeros(500)
for i in range(0, 500):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)
numpy.save("Data/BackLeg.npy", backLegSensorValues)
numpy.save("Data/FrontLeg.npy", frontLegSensorValues)
p.disconnect()