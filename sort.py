def array_sort(array): 
    newArray = [None] * len(array)
    for x in range(len(array)):
        newArray[array[x]] = array[x]
    return newArray




#scrambled array 
array1 = [0,4,1,3,2]
print(array_sort(array1))


