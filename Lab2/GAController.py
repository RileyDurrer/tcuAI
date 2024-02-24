import GAModel
generations=100
def runGenerations(generations):
    bestOfGen=[]
    currentGen = GAModel.initialize()
    for i in range (1, generations):
        currentGen=nextGen(currentGen)
    
    return 

def nextGen(currentGen):
    selectedGen = GAModel.selection(currentGen)
    