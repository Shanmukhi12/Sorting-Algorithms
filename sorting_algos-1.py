import random
from datetime import datetime

#Code for Insertion Sort

def insertionSort(A,low,high):
    for i in range(low+1,high):
        temp = A[i]
        k=i
        while k>0 and temp<A[k-1]:
            A[k]=A[k-1]
            k=k-1
        A[k] = temp
    return A


#Code for Merge Sort

def mergeSort(A):
    if len(A)>1:
        mid = len(A)//2
        lefthalf=A[:mid]
        righthalf=A[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                A[k]=lefthalf[i]
                i=i+1
            else:
                A[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            A[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            A[k]=righthalf[j]
            j=j+1
            k=k+1
    return A

#Code for HeapSort

def heap(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heap(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)
    return arr


#Code for In-Place Quick Sort

def partition(arr,l,h):
   i = ( l - 1 )
   x = arr[h]
   for j in range(l , h):
      if arr[j] <= x:
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[h] = arr[h],arr[i+1]
   return (i+1)

def quickSortIterative(arr,l,h):

  size = h - l + 1
  stack = [0] * (size)
  top = -1
  # push initial values
  top = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h
  # pop from stack
  while top >= 0:
    # Pop
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1
    # Set pivot element at its correct position
    p = partition( arr, l, h )
    # elements on the left
    if p-1 > l:
        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = p - 1
    # elements on the right
    if p+1 < h:
        top = top + 1
        stack[top] = p + 1
        top = top + 1
        stack[top] = h
  return arr

  
#Code for Modified quicksort  

def quick_sort(A,low,high):
    if low+7<high:
        partition_point=partition(A,low,high)
        quick_sort(A,low,partition_point-1)
        quick_sort(A,partition_point+1,high)
    else:
        A = insertionSort(A,low,high+1)
    return A

# Function for calculating Median
def median_of_three(mid,low,high):
    return(sorted([mid,low,high])[1])

# Function for returning partition index with pivot element median
def partition(A,low,high):

    pivot = median_of_three(A[(low+high-1)//2],A[low],A[high-1])
    pivotindex = A.index(pivot)       #only works if all values in array unique
    A[pivotindex] = A[low]
    A[low] = pivot
    left=low+1
    right=high
    done=False
    while not done:
        while left <= right and A[left] <= pivot:
            left=left+1
        while A[right] >= pivot and right >= left:
            right = right -1
        if right < left:
            done = True
        else:
            temp = A[left]
            A[left] = A[right]
            A[right]=temp
    temp=A[low]
    A[low] = A[right]
    A[right]=temp
    return right


number_of_elements = int(input("Enter input size of list :"))
list_type = input("Choose a Sorting Algorithm: \n a. Random List \n b. Sorted List \n c. Reverse Sorted List \n")

# To generate a random list
random_list = random.sample(range(1,number_of_elements+1),number_of_elements)

if(list_type == "a"):
  input_list = random_list
elif(list_type == "b"):
  input_list = sorted(random_list)  # sorting random list
elif(list_type == "c"):
  input_list = sorted(random_list)
  input_list.reverse()              # reversing sorded list
print(input_list)

start_time = datetime.now()
sorted_list = insertionSort(input_list,low=0,high=len(input_list))
time_taken = ((datetime.now() - start_time).total_seconds()) * 1000
print("time taken for insertionSort : ",time_taken)
print("sorted list : ",sorted_list)

start_time = datetime.now()
sorted_list = mergeSort(input_list)
time_taken = ((datetime.now() - start_time).total_seconds()) * 1000
print("time taken for mergeSort : ",time_taken)
print("sorted list : ",sorted_list)

start_time = datetime.now()
sorted_list = heapSort(input_list)
time_taken = ((datetime.now() - start_time).total_seconds()) * 1000
print("time taken for heapSort : ",time_taken)
print("sorted list : ",sorted_list)


start_time = datetime.now()
sorted_list = quick_sort(input_list,0,len(input_list)-1)
time_taken = ((datetime.now() - start_time).total_seconds()) * 1000
print("time taken for Modified quick_sort : ",time_taken)
print("sorted list : ",sorted_list)


start_time = datetime.now()
sorted_list = quickSortIterative(input_list, 0, number_of_elements-1)
time_taken = ((datetime.now() - start_time).total_seconds()) * 1000
print("time taken for In-place quick_sort : ",time_taken)
print("sorted list : ",sorted_list)