import GAModel
#How many generations does it go through
generations=100

#runs all the generations
def runGenerations():
    #collects best score of each generation
    bestOfGen=[]
    #creates first gen
    currentGen = GAModel.initialize()
    #rest of generations
    for i in range (0, generations):
        #sorts gen
        selectedGen = GAModel.selection(currentGen)
        #appends top agents score
        bestOfGen.append(GAModel.getValue(selectedGen[1]))
        #creates next generation and sets current gen to the next generation
        currentGen = GAModel.reproduceGen(selectedGen)
    
    #output = "Best of Each Generation: \n"
    #i=1
    #for agent in bestOfGen:
    #    output=output+f"Gen {i}: {round(GAModel.getValue(agent))}\n"
    #    i = i + 1
    
    return bestOfGen

