import os
import parallelHillClimber as hc

phc = hc.PARALLEL_HILL_CLIMBER()
os.system('rm 1')
phc.Evolve()
phc.Show_Best()
phc.record.close()
os.system('rm 1')
