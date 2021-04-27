import os
from typing import Dict

import solution
import constants as c
import copy

from solution import SOLUTION


class PARALLEL_HILL_CLIMBER:
    children: Dict[str, SOLUTION]

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.record = open('evolutionHistory.txt', 'w')
        self.generationId = 0
        self.parents = {}
        self.nextAvailableID = 0
        for x in range(c.populationSize):
            self.parents[str(x)] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(0, c.numberOfGenerations):
            self.generationId = currentGeneration
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    @staticmethod
    def Evaluate(solutions):
        for x in solutions:
            solutions[x].Start_Simulation(False)
        for x in solutions:
            solutions[x].Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents:
            if ((self.children[key].fitness > self.parents[key].fitness) or (self.parents[key].fitness==0)) and self.children[key].fitness != 0:
                self.parents[key] = self.children[key]

    def Show_Best(self):
        best = None
        bestK = None
        for key in self.parents:
            if best is None:
                best = self.parents[key]
                bestK = key
            else:
                if best.fitness < self.parents[key].fitness:
                    best = self.parents[key]
                    bestK = key
        if best is not None:
            self.record.write('\nBest solution set:'+bestK+' fitness:'+str(best.fitness))
            best.Start_Simulation(True)

    def Print(self):
        record = "Generation " + str(self.generationId) + ":\n"
        print("\nGeneration " + str(self.generationId) + ":")
        for key in self.parents:
            record += "Set"+key+" [P:<" + str(self.parents[key].fitness) + "> C:<" + str(self.children[key].fitness) + ">]\n "
            print("P:<" + str(self.parents[key].fitness) + "> C:<" + str(self.children[key].fitness) + ">")
        self.record.write(record)
