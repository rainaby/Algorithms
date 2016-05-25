class Node:
    def __init__(self):
        self.key=None
        self.right=None
        self.left=None
        self.parent=None
    
    
     
class Bst:
    
    def __init__(self):
        self.root = None

    def findMax(self,node):
        while(node.right!=None):
            node=node.right
            return node

    def findMin(self,node):
        while(node.left!=None):
            node=node.left
            return node
    
    def findSuccessor(self,node):
        if (node.right!=None):
            return findMin(node.right)
        else:
            p=node.parent
            x=node
            while(p!=None and x==p.right):
                x=p
                p=p.parent

            return p
        
    def searchNode(self,key):
        curr=self.root
        while(curr.key!=key or curr==None):
            if (curr.key<key):
                curr=curr.right
            else:
                curr=curr.left
        return curr

    def insertNode(self,key):
        x=self.root
        if (x==None):
            x=Node()
            x.key=key
            self.root=x
            return 

        while(x!=None):
            p=x
            
            if (key>x.key):
                x=x.right
            else:
                x=x.left
            
        x=Node()
        x.parent=p
        x.key=key 

        if (p.key>x.key):
            p.left=x
        else:
            p.right=x
        return

    def deleteNode(self,key):
        print ""
        return

    def printInOrder(self,x):
        if(x!=None):
            self.printInOrder(x.left)
            print x.key,x.parent.key if(x.parent) else None
            self.printInOrder(x.right)
        return

tree=Bst()
tree.insertNode(5)
tree.insertNode(4)
tree.insertNode(6)
tree.insertNode(100)
tree.insertNode(3)
tree.insertNode(78)
tree.insertNode(66)

tree.printInOrder(tree.root)
