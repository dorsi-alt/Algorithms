num_array = list()

num = int(input("Enter how many elements do you need to sort:\n"))

print('Enter numbers in array: ')

for i in range(int(num)):

    i = int(input("num :"))

    num_array.append(int(i))


def doStuff(alist):
    print(alist)
    halfalist = len(alist) // 2
    print("Middle Number(s)")
    if(len(alist)%2==0):
        print(alist[halfalist-1])
        print(alist[halfalist])   
        
        print("WTF")   
    else:
        print(alist[halfalist])

    print("THE FIRST AND LAST LETTER")

    print(alist[0])
    print(alist[num-1])

    print("EVERY ODD INDEXED NUMBER")
    for list in alist:
        if alist.index(list)%2!=0:
            print(list)


    #print(alist[len(alist)])
    
   
    # if(halfalist%2)==0:
    #     print(alist[halfalist])
    #     print(alist[halfalist+1])
    # if(halfalist%2) == 1:
    #     print(alist[halfalist+1])
    # return alist




doStuff(num_array)