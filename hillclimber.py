import solution
import constants as c
import copy


class HILL_CLIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()

    def Evolve(self):
        show = False
        self.parent.Evaluate(show)
        for currentGeneration in range(0, c.numberOfGenerations):
            if currentGeneration == c.numberOfGenerations-1:
                show = True
            self.Evolve_For_One_Generation(show)

    def Evolve_For_One_Generation(self, show):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(show)
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        pass

    def Mutate(self):
        self.child.Mutate()
        pass

    def Select(self):
        print("\nP=" + str(self.parent.fitness) + " : C=" + str(self.child.fitness))
        if self.child.fitness <= self.parent.fitness:
            self.parent = self.child
