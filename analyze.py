import numpy
import matplotlib.pyplot as mp

backLegSensorValues = numpy.load("Data/BackMotor.npy")
frontLegSensorValues = numpy.load("Data/FrontMotor.npy")
mp.plot(backLegSensorValues, label = "Back Leg")
mp.plot(frontLegSensorValues, label = "Front Leg")
mp.legend()
mp.savefig("HWMedia/HW4plot.png")