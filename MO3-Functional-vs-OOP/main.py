# Dutch National Flag ALgorithm

class solution:
    def sort012(self,arr,n):
            low=0
            high=n-1
            mid=0
        
        #iterating until mid pointer is less than or equal to high.
            while mid<=high:
            
            # if element at mid is 0, swap with element at low and move both pointers.
                if arr[mid]==0:
                    arr[mid] , arr[low] = arr[low] , arr[mid]
                    mid+=1
                    low+=1
                
            #if element at mid is 1, move mid pointer.
                elif arr[mid]==1:
                    mid+=1
                
            #if element at mid is 2, swap with element at high and move high pointer.
                else:
                    arr[mid] , arr[high] = arr[high] , arr[mid]
                    high-=1

# Binary search

class Solution:	
	def bin_search(self, arr, left, right, key):
		#check if left index is greater than right index
		#which means key is not found in the array
		if left > right:
			return -1
		
		#calculate the middle index
		mid = (left + right) // 2
		
		#check if the element at the middle index is equal to the key
		if arr[mid] == key:
			return mid
		
		#if the element is greater than the key, 
		#we search in the left half of the array
		elif arr[mid] > key:
			return self.bin_search (arr, left, mid - 1, key)
		
		#if the element is smaller than the key,
		#we search in the right half of the array
		else:
			return self.bin_search (arr, mid + 1, right, key)
	
	def binarysearch(self, arr, n, k):
		#call the recursive binary search function
		return self.bin_search(arr, 0, n-1, k)
