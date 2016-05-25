# Insertion Sort
from random import *

MAXVALUE=99

class InsertionSort:
	
	def __init__(self,list):
		for i in range(1,len(list)):
			key=list[i]
			j=i-1
			while(j>=0 and list[j]>key):
				list[j+1]=list[j]
				j=j-1
				#print list
			list[j+1]=key
                        
                        #print list
		print "Insertion Sort Output is:\n" + str(list) 	
	
class MergeSort:
	def __init__(self,list):
		print "\nOriginal list is"		
		print list
		self.array=list
		self.p=0
		self.r=len(list)-1
		self.mergeSort(self.p,self.r)
		print "Output of Merge Sort is" ,(self.array)
		
	def merge(self,p,q,r):
		n1=q-p+1
		n2=r-q
		
		j=0
		L=[]
		R=[]
		for i in range(p,q+1):
			L.append(self.array[i])
			j+=1
		L.append(MAXVALUE)
		j=0
		
		for i in range(q+1,r+1):
			R.append(self.array[i])
			j+=1
			
		R.append(MAXVALUE)
		i=0
		j=0
		
		for k in range(p,r+1):
			if L[i]<=R[j]:
				self.array[k]=L[i]
				i+=1
			else:
				self.array[k]=R[j]
				j+=1
		
	def mergeSort(self,p,r):
		if p<r:
			#print self.array
			q=(p+r)/2
			self.mergeSort(p,q)
			#print self.array
			self.mergeSort(q+1,r)
			#print self.array
			self.merge(p,q,r)
			#print p,q,r
			print "Output of intermediate step is" 
			print self.array

	

list=[9,2,4,1,9,3,6,5,8]
IS=InsertionSort(list)	

list=[9,2,4,1,9,5,3,8,6]
MS=MergeSort(list)	
