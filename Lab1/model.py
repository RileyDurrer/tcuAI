from queue import Queue

class node:
    def __init__(self, data):
      self.data= data 
      self.children= []
      
    def addChild(self, child):
      self.children.append(child)
      
global root 
root = node(0)
path=[]


def addNode(data, parent):
  if (BFS(data)):
    return False
  if (BFS(parent)):
    path[-1].addChild(data)
    print("added")
    return True
  else:
    print("couldn't find parent")
    return

  
def BFS(target):
  
  def rBFS(node, target):
    path.append(node)
    if(node.data==target):
      return True
    for child in node.children:
      q.put(child)
    if (q.empty):
      return False
    else:
      return rBFS(q.get, target)
  path=[]
  q = Queue
  return rBFS(root, target)
    

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
  



       
