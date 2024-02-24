import random

#number 0-10 that control how strong a mutation can be
mutationStDev = 1
#how far x y or z can go in either direction
geneRange= 100
population=100

currentGeneration= initialGeneration()

class agent:
    def __init__(self, parent):
        if (parent):
            self.x= parent.x.mutate
            self.y= parent.y.mutate
            self.z= parent.z.mutate
        value= self.score()
        pass
    
    def reproduce(self):
        agent
    

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
        return (a* self.x**2 + b * self.y**2 + c * self.z**2)
    



def initialGeneration:
    