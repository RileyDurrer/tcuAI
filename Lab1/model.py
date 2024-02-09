from queue import Queue

#node object
class node:
    def __init__(self, data):
      self.data= data 
      self.children= []
      
    def addChild(self, child):
      self.children.append(child)

      

root = node("0")
#records the path each search takes so controller can use it
path=[]

#adds a new node and returns true if it can
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
    
#searches via depth
def DFS(target):
  path.clear()
  
  #recursivly calls itself to go through all children
  def rDFS(currentNode, target):
    path.append(currentNode)
    if (currentNode==target):
      return True
    for child in currentNode.children:
      if (rDFS(child, target)):
        return True
    return False
  
  return rDFS(root, target)

#searches the tree via depth but depth increases every time
def IDS (target):
  path.clear() 
  for depth in range(6):
    if DLS(root, target, depth):
      return True
  return False

#the search at each depth  
def DLS(currentNode, target, depth):
  path.append(currentNode)
  if depth == 0 and currentNode.data == target:
      return True
  elif depth > 0:
    for child in currentNode.children:
      if DLS(child, target, depth - 1):
        return True
  return False
  



       
