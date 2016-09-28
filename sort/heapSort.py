class HeapSort:
	def __init__(self,array):
		self.target=array
		self.length=len(array)
		self.hsz=self.length-1
		

	def left(self,i):
		return 2*i+1
	
	def right(self,i):
		return 2*i+2
	
	def swap(self,i,j):
		temp=self.target[i]
		self.target[i]=self.target[j]
		self.target[j]=temp

	def maxHeapify(self,start):
		l=self.left(start)
		r=self.right(start)
		#print l,r
		i=start
		if l<=self.hsz and self.target[l]>self.target[i]:
			larg=l
		else:
			larg=i
		
		if r<=self.hsz and self.target[r]>self.target[larg]:
			larg=r
		
		if larg!=i:
			self.swap(larg,i)
			self.maxHeapify(larg)
			#print self.target

	
	def buildMaxheap(self):
		for i in range(self.length/2-1,-1,-1):
			self.maxHeapify(i)
		#print self.target

	def heapSort(self):
		self.buildMaxheap()
		print 'done'
		for i in range(self.length-1,0,-1):

			self.swap(0,i)
			#print self.target, 'swapp'
			self.hsz-=1
			self.maxHeapify(0)
		return self.target

sort=[5,4,3,222,31,23,77,53,245,8,95,3,3246,8,9,97,6544,22,6]
heapSort=HeapSort(sort)

print heapSort.heapSort()