import pybullet as p
import pybullet_data, time, os
#os.system("python3 generate.py")
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
for i in range(0, 1500):
    p.stepSimulation()
    time.sleep(1/60)
p.disconnect()