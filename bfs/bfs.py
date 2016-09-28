from graphPackage import graph

net=graph()
n1=net.addNode(5)
n2=net.addNode(6)
n3=net.addNode(8)

net.addEdge(n1,n2)

net.print1()
