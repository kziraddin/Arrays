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
    


    """NOTE:
    when we run the unit tests for our functions, error messages that we include in our functions are popping up in our output
    We want to suppress the print statements during testing. We will modify our functions to use logging instead of print"""