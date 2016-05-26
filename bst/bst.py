import drawtree
import os
import time
import sys

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
            return self.findMin(node.right)
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

    def transplant(self,x,y):
        
        if (x.parent==None):
            self.root=y
            return
        
        if (x.parent.left==x):
            x.parent.left=y
        else:
            x.parent.right=y
        
        if (y!=None):
            y.parent=x.parent
        return
        
    def deleteNode(self,key):
        if (self.searchNode(key)):
            x=self.searchNode(key) 
        else:
            print "Key not found"
            return

        if(x.right==None):
            self.transplant(x,x.left)
        elif(x.left==None):
            self.transplant(x,x.right)
        else:
            succ= self.findMin(x.right)
            if (succ.parent!=x):
                succ=self.findSuccessor(x)
                self.transplant(succ,succ.right)
                succ.right=x.right
                succ.right.parent=succ
            self.transplant(x,succ)
            succ.left=x.left
            succ.left.parent=succ
        return
    
    def printInOrder(self,x):
        if(x!=None):
            self.printInOrder(x.left)
            print x.key,x.parent.key if(x.parent) else None
            self.printInOrder(x.right)
        return

    def preOrder(self,x):
        global orderList

        if(x!=None):
           
            if(x.key):
                orderList.append(x.key)
            self.preOrder(x.left)
            self.preOrder(x.right)
        return


os.system("clear")
print "                                                                                Welcome to BSTMAKER by Abhay Raina                                                              "
tree=Bst()
inp=tree.insertNode(int(raw_input("Please enter the numeric key for the root node.\n")))
while(not str(inp)=="end"):
    inp=raw_input("Write 'in' to insernode and 'del' to remove node 'end' to stop BSTMAKER.\n")
    
    if (inp=="in"):
        tree.insertNode(int(raw_input("Write the numeric key of the node to insert.\n")))   
    elif (inp=="del"):
        tree.deleteNode(int(raw_input("Write the numeric key of the node to delete.\n")))
    elif (inp=="end"):
        break
    else:
        print("Wrong input program try again....")
    
    print("\......................................................................................................................................................\n")
    orderList=[]
    tree.preOrder(tree.root)
    drawtree.draw_bst(orderList) 
    #print orderList
    print("\n\......................................................................................................................................................\n")
print"\nThank you"
count=10
print "Shuting Down.",
while(count!=0):
    sys.stdout.write( "." )
    sys.stdout.flush()
    time.sleep(0.25)
    sys.stdout.flush()
    count-=1

os.system("clear")

