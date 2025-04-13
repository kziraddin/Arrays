def printElements(arr):
    return arr

    
def insertAtEnd(arr, val, length, capacity):
    if length < capacity:
        arr[length] = val
        return True
    else:
        print("\nCannot insert. Array is full.")
        return False


def insertAtBeginning(arr, val, length, capacity):
    if length < capacity:
        # shift elements to the right
        for i in range(length - 1, -1, -1):
            arr[i + 1] = arr[i]
        arr[0] = val
        return True
    else:
        print("\nCannot insert. Array is full.")
        return False

# add value at a specific index
def insertAtIndex(arr, val, i, length, capacity):
    if i < 0 or i > length:
        print("\nOut of range.")
        return False

    if length >= capacity:
        print("\nCannot insert. Array is full.")
        return False

    # shift elements to the right from requested index included
    for index in range(length-1, i - 1, -1):
        arr[index+1] = arr[index]

    # assign a value at requested position
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

if __name__ == '__main__':
    
    print("\n")
    capacity = int(input("Enter max length of array: >>  ")) # allocating memory in advance.
    arr = [0] * capacity # preallocate array with fixed size
    length = 0 # initialy, no valid elements

    while True:
        print("\n")
        print("\n Press 0 to Quit!")
        print("\nPress 1 to ADD a value at the beginning of the list.")
        print("\nPress 2 to ADD a value at the end of the list.")
        print("\nPress 3 to ADD a value at a desired position.")
        print("\nPress 4 to REMOVE a value from end.")
        print("\nPress 5 to REMOVE a value from desired position.")
        print("\nPress 6 to SORT the list.")
        print("\n")

        choice = input("\nChoose an option: >>  ")
        if choice == "1":
            print("\nCurrent List:")
            print(printElements(arr))
            val = int(input("\nEnter the value to add: >>  "))
            success = insertAtBeginning(arr, val, length, capacity)
            if success:
                length += 1
                print("\nUpdated List:")
                print(printElements(arr))
                print("\n")

        elif choice == "2":
            print("\nCurrent List:")
            print(printElements(arr))
            val = int(input("\nEnter the value to add: >>  "))
            success = insertAtEnd(arr, val, length, capacity)
            if success:
                length += 1
                print("\nUpdated List:")
                print(printElements(arr))
                print("\n")

        elif choice == "3":
            print("\nCurrent List:")
            print(printElements(arr))

            i = int(input("Enter desired index: >>  "))
            val = int(input("\nEnter value to add: >>  "))

            success = insertAtIndex(arr, val, i, length, capacity)
            if success:
                length += 1
                print("\nUpdated List:")
                print(printElements(arr))
                print("\n")
        
        elif choice == "4":
            print("\nCurrent List:")
            print(printElements(arr))
            success = removeEnd(arr, length)
            if success:
                length -= 1
                print("\nUpdated List:")
                print(printElements(arr))
                print("\n")

        elif choice == "5":
            print("\nCurrent List:")
            print(printElements(arr))
            i = int(input("\nEnter the index: >>  "))
            success = removeAtIndex(arr, i, length)
            if success:
                length -= 1
                print("\nUpdated List:")
                print(printElements(arr))
                print("\n")
        elif choice == "6":
            print("\nCurrent List:")
            print(printElements(arr))
            sorted_list = sortArray(arr)
            print("\nUpdated List:")
            print(printElements(sorted_list))
            print("\n")

        elif choice == "0":
            break