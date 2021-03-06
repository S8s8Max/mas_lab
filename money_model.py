from mesa import Agent, Model
from mesa.time import RandomActivation

class MoneyAgent(Agent):
    """ an agent with fixed initial wealth. """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        print("hi, i am " + str(self.unique_id))

class MoneyModel(Model):
    """ a model with some number of agents """
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)

        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        self.schedule.step()


