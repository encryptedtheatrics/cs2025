def quick_sort(L):
    left_list = []
    middle_list = []
    right_list = []
    # Base case
    if len(L) <=1:
        return(L)
    # Set pivot to the last element in the list
    pivot = L[len(L)-1]
    # Iterate through all elements (keys) in L
    for key in L:
        if key < pivot:
            left_list.append(key)
        elif key == pivot:
            middle_list.append(key)
        else:
            right_list.append(key)
    # Repeat the quicksort on the sub-lists and combine the results
    return quick_sort(left_list) + middle_list + quick_sort(right_list)

print(quick_sort([1, 4, 5, 6, 2, 3, 5, 1 , 45, 5, 12, 123, 432, 466]))