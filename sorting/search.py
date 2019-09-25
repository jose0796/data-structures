####################################################################
###
### Author: Jose Moran 
### Email : jmoran071996@gmail.com
### Github: jose0796
### Description: Binary search implementation and description
###
####################################################################


def binary_search(a,x):

    """ 
        Binary Search algorithm

        This is a divide-conquer strategy algorithm.
        It assumes the array given is already sorted, 
        and based on this asssumption reduces the portion
        of the array to be search exponentially. 


        a = [a[s], ... , a[m], ... , a[e]], x
                           |
                          a[m] > x ? 
        
        this implies that 
            a = [a[m+1], ... , a[e]], s = m+1

        we do this recursively until its narrowed down to a 
        soul element. 

        time-complexity:
            best-case: O(1)
            avg-case : O(log n)
            worst-case: O(log n)
        
        space-complexity: O(1)



    """


    s = 0
    e = len(a)-1
    

    while s < e:
        mid = s+e//2
        if a[mid] == x:
            return mid
        
        if a[mid] < x:
            s = mid+1
        else:
            e = mid-1
    
    return -1

