import random
import numpy as np

#number 0-10 that control how strong a mutation can be
mutationStDev = 1
#how far x y or z can go in either direction
geneRange= 100
population=100
#determans how likliy the first agent is to be picked for reproduction (the lower the more diverse the next generation will be)
probability=.01
elitism = 0



class Agent:
    def __init__(self, x, y, z):
        self.x= x
        self.y= y
        self.z= z
        self.value= self.score()
    
    def reproduce(self):
        x=self.mutate(self.x)
        y=self.mutate(self.y)
        z=self.mutate(self.z)
        return Agent(x,y,z)
    
    
    @staticmethod
    def mutate(gene):
        mutation = random.gauss(gene, mutationStDev)
        if (mutation>geneRange):
            mutation=geneRange
        elif (mutation<(geneRange*-1)):
            mutation= geneRange*-1
        return mutation
    
    def score(self):
        #constants
        a = 3
        b = 4
        c = 1/4
        #the algorithim
        return -(100 * (self.y - self.x**2)**2 + (1 - self.x)**2 + 100 * (self.z - self.y**2)**2)
    
#Grabs the value of a given agent, used for sorting key    
def getValue(Agent):
        return Agent.value


def initialize():
    agents=[]
    for agent in range(population):
      agent=Agent(random.uniform(-1, 1)*geneRange,
                  random.uniform(-1, 1)*geneRange,
                  random.uniform(-1, 1)*geneRange) 
      agents.append(agent)
   
    return agents

def selection(agents):
    sortedAgents = sorted(agents, key=lambda Agent: Agent.value, reverse=True)
    return sortedAgents

def reproduceGen(parents):
    nextGen=parents[0:elitism]
    while (len(nextGen)<population):
        for parent in parents:
            if (random.random() < probability):
                nextGen.append(parent.reproduce())
                break
    return nextGen
        
