import GAModel
generations=100
def runGenerations(generations):
    bestOfGen=[]
    currentGen = GAModel.initialize()
    for i in range (1, generations):
        selectedGen = GAModel.selection(currentGen)
        bestOfGen.append(selectedGen[1])
        currentGen = GAModel.reproduceGen(selectedGen)

    
    return 

def nextGen(parentGen):
    

    return childGen()