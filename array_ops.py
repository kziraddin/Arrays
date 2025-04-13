import logging

logging.basicConfig(level=logging.INFO)

def printElements(arr):
    return arr

    
def insertAtEnd(arr, val, length, capacity):
    if length < capacity:
        arr[length] = val
        return True
    else:
        logging.info("\nCannot insert. Array is full.")
        return False


def insertAtBeginning(arr, val, length, capacity):
    if length < capacity:
        for i in range(length - 1, -1, -1):
            arr[i + 1] = arr[i]
        arr[0] = val
        return True
    else:
        logging.info("\nCannot insert. Array is full.")
        return False


def insertAtIndex(arr, val, i, length, capacity):
    if i < 0 or i > length:
        logging.info("\nOut of range.")
        return False

    if length >= capacity:
        logging.info("\nCannot insert. Array is full.")
        return False

    for index in range(length-1, i - 1, -1):
        arr[index+1] = arr[index]

    arr[i] = val
    return True
    

def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0
        return True
    return False


# remove at specified position
def removeAtIndex(arr, i, length):
    if i < 0 or i >= length:
        print("\nInvalid index.")
        return False
    
    for index in range(i, length - 1):
            arr[index] = arr[index + 1]

    arr[length - 1] = 0
    return True # to update length




def sortArray(array):
    
    def mergeSort(arr):
        if len(arr) <= 1:
            return arr
    
        mid = (len(arr)) // 2

        left_arr = mergeSort(arr[:mid])
        right_arr = mergeSort(arr[mid:])
    
        return merge(left_arr, right_arr)

    def merge(left, right):
        merged = []
        i = 0 # for left array
        j = 0 # for right array

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # could be remaining elements 
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    return mergeSort(array)
