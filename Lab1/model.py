from queue import Queue

class node:
    def __init__(self, data):
      self.data= data 
      self.children= []
      
    def addChild(self, child):
      self.children.append(child)
      

root = node("0")
path=[]


def addNode(data, parent):
  if (BFS(data)):
    print("test")
    return False
  if (BFS(parent)):
    path[-1].addChild(node(data))
    print("added")
    print(path)
    return True
  else:
    print("couldn't find parent")
    return False

  
def BFS(target):
  path.clear()
  # Initialize a queue and add the root node to it
  q = Queue()
  q.put(root)
    
    # Iterate as long as the queue is not empty
  while not q.empty():
    # Get the next node from the queue
    currentNode = q.get()
    path.append(currentNode)
    print(currentNode.data+"on path")
        
    # Check if this is the target node
    if currentNode.data == target:     
      print(f"Found: {currentNode.data}")
      return True
        
      # Otherwise, add its children to the queue for further searching
    for child in currentNode.children:
      q.put(child)
    
  # If we reach this point, the target was not found
  print("Target not found.")
  return False
    

def DFS(target):
  #for child in node.children:
   #     path.append(child.data)
   #     return True
   #   else:
   #     rBFS(child, target)
  pass


def IDS (target):
   
  #def rBFS(node, target):
   # for child in node.children:
    #  if child.data == target:
    #    path.append(child.data)
    #    return True
    #  else:
    #    q.put(child)

  #q = Queue
  #return rBFS(root, target)
  
  pass
  



       
