import model
root = model.root.data

path=model.path

nodes =[root]
output=""

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
            output= f"{target} doesn't exist"
    output= "Path ="
    for node in path:
        output=output+" "+ node.data +"-->"
    output=output+" finish"
    
        

def createNode(value, parent):
    print("attempt to add")
    if(model.addNode):
        output=f"{value} added"
        nodes.append(value)
    else:
        output=f"{value} already exists"
