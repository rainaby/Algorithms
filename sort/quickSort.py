class QuickSort:
	def __init__(self,arr):
		self.arr=arr
	def swap(self,i,j):
		temp=self.arr[j]
		self.arr[j]=self.arr[i]
		self.arr[i]=temp

	def partition(self,start,end):
		pivot=self.arr[end]
		i=start-1
		for j in range(start,end):
			if pivot>=self.arr[j]:
				i=i+1
				self.swap(i,j)
		self.swap(i+1,end)
		return i+1

	def quickSort(self,start,end):
		if start<end:
			mid=self.partition(start,end)
			self.quickSort(start,mid-1)
			self.quickSort(mid+1,end)
		return self.arr
	
q=QuickSort([3,213,213,123,4,1245,5123,123,4,13])

print q.quickSort(0,9)


