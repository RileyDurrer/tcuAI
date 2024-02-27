import random
import numpy as np

#number 0-10 that control how strong a mutation can be
mutationStDev = 1
#how far x y or z can go in either direction
geneRange= 100
#how many agents in a generation
population=100
#determans how likliy the first agent is to be picked for reproduction (the lower the more diverse the next generation will be)
probability=.05
#determines how many of the top agents of a generation are kept
elitism = 4


#class that represents agents in a generation, they hold 3 variables and are scored based on an equation
class Agent:
    def __init__(self, x, y, z):
        self.x= x
        self.y= y
        self.z= z
        #scores agent based on a function that uses the variables
        self.value= self.score()
    
    def reproduce(self):
        #mutates each gene of an agent to create a new agent
        x=self.mutate(self.x)
        y=self.mutate(self.y)
        z=self.mutate(self.z)
        return Agent(x,y,z)
    
    
    @staticmethod
    def mutate(gene):
        #uses normal distribution to randomize the genes in a way that prefers being close but doesnt need to be
        mutation = random.gauss(gene, mutationStDev)
        #keeps the genes in the range
        if (mutation>geneRange):
            mutation=geneRange
        elif (mutation<(geneRange*-1)):
            mutation= geneRange*-1
        return mutation
    
    def score(self):
        #constants if applicable
        a = 3
        b = 4
        c = 1/4
        #the algorithim
        return -(100 * (self.y - self.x**2)**2 + (1 - self.x)**2 + 100 * (self.z - self.y**2)**2)
    
#Grabs the value of a given agent, important for sorting key    
def getValue(Agent):
        return Agent.value

#creates genisis generation by populating it randomly
def initialize():
    agents=[]
    for agent in range(population):
      agent=Agent(random.uniform(-1, 1)*geneRange,
                  random.uniform(-1, 1)*geneRange,
                  random.uniform(-1, 1)*geneRange) 
      agents.append(agent)
   
    return agents

#sorts generation by agents value
def selection(agents):
    sortedAgents = sorted(agents, key=lambda Agent: Agent.value, reverse=True)
    return sortedAgents

#creates next generation out of current generation
def reproduceGen(parents):
    #grabs top agents from last gen
    nextGen=parents[0:elitism]
    #adds agents until they equal population size
    while (len(nextGen)<population):
        #goes through sorted list until random selection is successful so it prioritizes fitter agents (easy to change to what degree with variable probability)
        for parent in parents:
            if (random.random() < probability):
                nextGen.append(parent.reproduce())
                break
    return nextGen
        
