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
        for i in range(length - 1, -1, -1):
            arr[i + 1] = arr[i]
        arr[0] = val
        return True
    else:
        print("\nCannot insert. Array is full.")
        return False


def insertAtIndex(arr, val, i, length):
    if i < 0 or i > length:
        print("\nOut of range.")
        return False

    if length >= capacity:
        print("\nCannot insert. Array is full.")
        return False

    for index in range(length-1, i - 1, -1):
        arr[index+1] = arr[index]

    arr[i] = val
    return True
    






if __name__ == '__main__':
    
    print("\n")
    capacity = int(input("Enter max length of array: >>  ")) # allocating memory in advance.
    arr = [-1] * capacity # preallocate array with fixed size
    length = 0 # initialy, no valid elements

    while True:
        print("\n")
        print("\n Press 0 to Quit!")
        print("\nPress 1 to ADD a value at the end of the list.")
        print("\nPress 2 to ADD a value at a desired position.")
        print("\nPress 3 to ADD a value at the beginning of the list.")
        print("\n")

        choice = input("\nChoose an option: >>  ")

        if choice == "1":
            print("\nCurrent List:")
            print(printElements(arr))
            val = int(input("\nEnter the value to add: >>  "))
            success = insertAtEnd(arr, val, length, capacity)
            
            if success:
                length += 1
                print("\nUpdated List:")
                print(printElements(arr))
                print("\n")

        elif choice == "2":
            print("\nCurrent List:")
            print(printElements(arr))
            val = int(input("\nEnter value to add: >>  "))
            i = int(input("Enter desired position: >>  "))
            success = insertAtIndex(arr, val, i, length)

            if success:
                length += 1
                print("\nUpdated List:")
                print(printElements(arr))
                print("\n")
        
        elif choice == "3":
            print("\nCurrent List:")
            print(printElements(arr))
            val = int(input("\nEnter the value to add: >>  "))

            success = insertAtBeginning(arr, val, length, capacity)
            if success:
                length += 1
                print("\nUpdated List:")
                print(printElements(arr))
                print("\n")

        elif choice == "0":
            break