def SelectionSort(array,size):
    for item in range(size):
        min=item
        for j in range(item+1,size):
            if array[j]<array[min]:
                min=j
        (array[item],array[min])=(array[min],array[item])

