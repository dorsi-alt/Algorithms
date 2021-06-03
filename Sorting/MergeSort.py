num_array = list()

print("MERGE SORT ALGORITHM")

num = int(input("Enter how many elements do you need to sort:\n"))

print('Enter numbers in array: ')

for i in range(int(num)):

    i = int(input("num :"))

    num_array.append(int(i))

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              # merging back into one array
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j] 
                j += 1
            # Move to the next slot
            k += 1
        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

        print(myList)

mergeSort(num_array)