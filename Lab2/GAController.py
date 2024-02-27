import GAModel
generations=100
def runGenerations():
    bestOfGen=[]
    currentGen = GAModel.initialize()
    for i in range (0, generations):
        selectedGen = GAModel.selection(currentGen)
        bestOfGen.append(selectedGen[1])
        currentGen = GAModel.reproduceGen(selectedGen)
    
    output = "Best of Each Generation: \n"
    i=1
    for agent in bestOfGen:
        output=output+f"Gen {i}: {round(GAModel.getValue(agent))}\n"
        i = i + 1
    
    return output

