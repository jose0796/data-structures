
####################################################################
###
### Author: Jose Moran 
### Email : jmoran071996@gmail.com
### Github: jose0796
### Description: Basic to advanced sorting algorithms such as:
### bubblesort, insertion sort, quicksort, and linear-sorting 
### algorithms (counting sort, radix-sort, bucket-sort). Based on: 
### 
###  Intro to Algorithms,Thomas H. Cormen, 3rd Ed., pages 16-170
###  
###
###
####################################################################


def bubblesort(a):

    """ 
    
        Sorts the array a using bubble-like strategy

        a = [a[0], ... , a[i],  a[i+1], ... , a[n-1] ]
                           |_______|
                               |
                         if a[i] > a[i+1] 
                         ---> swap(a[i],a[i+1])

        1. swap a[i] and a[i+1] if a[i] > a[i+1],
           until there are no more swaps. 
        2. if no more swaps, then array is ordered.

        time-complexity: 
            best-case : O(n)
            aver-case : theta(n^2)
            worst-case: O(n^2)

        space-complexity: O(1)

    
    """

    while True:
        swap = 0
        for i in range(1,len(a)):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                swap = 1
        
        if not swap:
            break 



def insertion_sort(a):

    """ 
    
        Insertion Sort 

        1. Loop through entire array 
        2. On each element a[i] check a[i-j] < a[i], where 
            0<= j < i <= n
        3. If a[i-j] > a[i] then swap(a[i-j],a[i])
        4. When i == n the algorithm finishes with a ordered
    

        a = [a[0], ... , a[i-j], ... a[i], ... a[n-1]]
                            |__________|
                                  |
                           if a[i-j] > a[i]:
                               swap(a[i-j],a[i])
        
        time-complexity: 
            best-case : O(n)
            avg-case  : theta(n^2)
            worst-case: O(n^2)
        
        space-complexity: O(1)

                            
    
    """


    for i in range(1,len(a)):
        j = i
        while j:
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
            j-=1


def selectionsort(a):
    """ 
    
        Selection Sort 

        1. Select the minimun element of the subarray a[j:n], 
           where 0<= j <= n-1
        2. Make this loop n times. Then the algorithm finishes. 


        a = [a[0], a[1], ... a[n-2], a[n-1]]
              |__________________________|
                            |
                    swap(min(a[0:n]), a[0])

        then min(a) is swap with a[0]. Then 

        a = [min(a[0:n]), a[1], a[2], ... , a[n]]
                            |_________________|
                                     |
                            swap(min(a[1:n]), a[1])
        
                        ...

        a = [ min(a[0:n]), min(a[1:n]), min(a[2:n]), ... , min(a[n-1:n]) ]

        time-complexity: O(n^2)
        space-complexity: O(1)
    
    
    """
    j = 0

    while j < len(a):
        m = min(a[j:])
        i = a.index(m)
        a[i],a[j] = a[j],a[i]
        j+=1


def mergesort(a):

    """ 
    
        Merge Sort 

        It's a divide-and-conquer algorithm based on the idea 
        of breaking down a list into several sub-lists until 
        each sublists consists of a single element and merging
        those sublists in a manner that results into a sorted 
        list. 

        1. Divide the unsorted list into N sublists.
        2. Take adjacent pairs of two singleton lists and merge 
        them to form a list of 2 elements.
        3. Repeat step 2 until a single sorted list is obtained.


                   [a[s], a[s+1], ... , a[mid-1], a[mid], a[mid+1], ... , a[e-1], a[e] ]
                           ________________________|_______________________
                          |                                                |
             [ a[s],...,a[m] , ..., a[mid]]                 [ a[mid+1],..., a[m] , ..., a[e]]
                __________|__________                           ___________|___________
               |                     |                         |                        |
            a[s:m]               a[m+1:mid]                 a[mid+1:m]              a[m+1:e]
               |_____________________|                         |________________________|
                          |                                                |
             [ a[s],...,a[m] , ..., a[mid]]                 [ a[mid+1],..., a[m] , ..., a[e]]
                          |________________________________________________|
                                                    |
                  [a[s], a[s+1], ... , a[mid-1], a[mid], a[mid+1], ... , a[e-1], a[e] ]

        time-complexity: O(n log n)
        space-complexity: O(n)    
    
    
    """



    def merge(left,right):
        ll = len(left)
        lr = len(right)
        result = []
        i,j = 0,0
        while i < ll and j< lr:
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        result += left[i:]
        result += right[j:]
        return result 


    
        
    if len(a)<= 1:
        return a

    mid = len(a)//2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left,right)

    




def quicksort(a):

    """ 
        Quicksort 

        (Divide): Partition the array a[p..r] into two subarrays
        a[p..q-1] and a[q+1..r] such that each element of a[p..q-1]
        is less than or equal to a[q], which is, in turn, less than 
        or equal to each element of a[q+1..r]. 
        (Conquer): Sort the two subarrays a[p..q-1] and a[q+1..r] by
        recursive calls to quicksort. 
        (Combine): Subarrays are already sorted, no work is needed to 
        combine subarrays. 


        a = [a[p], ... , a[q-1], a[q], a[q+1] , ... , a[r]]
              |_____________|            |______________|
                     |                          |
                 a[p:q]      <   a[q]  <     a[q+1:r+1]

        
        call recursively quicksort with subarray a[p:q] and a[q+1:r+1]

        time-complexity:
            best-case: O(nlogn)
            avg-case : O(nlogn)
            worst-case: O(n^2)
        
        space-complexity: O(1)

    """


    def partition(a,s,e):
        x = a[e]
        i = s-1
        for j in range(s,e):
            if x >= a[j]:
                i+=1
                a[i],a[j] = a[j],a[i]
        i+=1
        a[i],a[e] = a[e], a[i]
        return i
    
    def __quicksort(a,s,e):
        if s <= e:
            q = partition(a,s,e)
            __quicksort(a,s,q-1)
            __quicksort(a,q+1,e)
        
    __quicksort(a,0,len(a)-1)


