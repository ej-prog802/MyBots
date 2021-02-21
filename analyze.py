import numpy
import matplotlib.pyplot as mp

backLegSensorValues = numpy.load("Data/BackLeg.npy")
frontLegSensorValues = numpy.load("Data/FrontLeg.npy")
mp.plot(backLegSensorValues, label = "Back Leg", linewidth = 2)
mp.plot(frontLegSensorValues, label = "Front Leg")
mp.legend()
mp.savefig("HWMedia/HW3plot.png")