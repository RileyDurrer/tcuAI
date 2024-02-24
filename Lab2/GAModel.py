import random

#number 0-10 that control how strong a mutation can be
mutationStDev = 1
#how far x y or z can go in either direction
geneRange= 100
population=100




class Agent:
    def __init__(self, x, y, z):
        self.x= x
        self.y= y
        self.z= z
        value= self.score()
    
    def reproduce(self):
        Agent
        pass
    
    
    
    
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
        return (a* self.x**2 + b * self.y**2 + c * self.z**2)

#Grabs the value of a given agent, used for sorting key    
def getValue(agent):
        return agent.value


def initialize():
    agents=[]
    for index in population:
      index=agent(random.uniform(-1, 1)*geneRange, random.uniform(-1, 1)*geneRange, random.uniform(-1, 1)*geneRange) 
      agents.append(index)
    return agents

def selection(agents):
    sortedAgents=sorted(agents, key=getValue, reverse=True)
    return sortedAgents[:50]