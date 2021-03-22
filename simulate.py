from simulation import SIMULATION
import os
os.system("python3 generate.py")
simulation = SIMULATION()
simulation.RUN()
# numpy.save("Data/FrontLeg.npy", frontLegSensorValues)
# numpy.save("Data/BackMotor.npy", backLegMotorValues)
# numpy.save("Data/FrontMotor.npy", frontLegMotorValues)
# p.disconnect()