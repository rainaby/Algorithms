class binaryNode:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        self.parent=None
    
class binaryTree:
    
    def __init__(self,rootKey):
        self.root=rootKey

    def addLeftChild(self,base,key):
        base.left=binaryNode(key)
        base.left.parent=base

    def addRightChild(self,base,key):
        base.right=binaryNode(key)
        base.right.parent=base

class graphNode:
    
    def __init__(self,key):
        self.key=key
        self.connections={}
      
               
class graph:
    
    def __init__(self):
        self.nodes={}
    
    def addNode(self,key):
        self.nodes[key]=graphNode(key)
        
    def addEdge(self,node1,node2):
        node1.connections[node2.key]=node2
        node2.connections[node1.key]=node1
    
    def print1(self):
        for each in self.nodes:
            print each.key,
            for each1 in each.connections:
                print each1.value.key







