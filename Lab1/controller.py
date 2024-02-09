import model
root = model.root.data

path=model.path

nodes =[root]

#finds search type and calls it returning the ouput
def search(target, type):
    if (type=="BFS"):
        if (model.BFS(target)):
            pass
        else:
            output= f"{target} doesn't exist"
    elif (type=="DFS"):
        if (model.DFS(target)):
            pass
        else:
            output= f"{target} doesn't exist"
    else:
        if (model.IDS(target)):
            pass
        else:
            output= f"{target} couldn't be found"
    output= "Path ="
    for nodes in path:
        output=output+" "+ nodes.data +"-->"
    return output+" finish"
    
        
#adds a node and returns the response
def createNode(value, parent):
    print("attempt to add")
    if(model.addNode(value, parent)):
        
        nodes.append(value)
        return f"{value} added under {parent}"
    else:
        return f"{value} already exists"
