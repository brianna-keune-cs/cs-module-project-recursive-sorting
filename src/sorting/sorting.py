# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a_index = 0
    b_index = 0
    index_count = 0

    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            merged_arr[index_count] = arrA[a_index]
            a_index += 1
            index_count += 1
        else:
            merged_arr[index_count] = arrB[b_index]
            b_index += 1
            index_count += 1
    while b_index < len(arrB):
        merged_arr[index_count] = arrB[b_index]
        b_index += 1
        index_count += 1
    while a_index < len(arrA):
        merged_arr[index_count] = arrA[a_index]
        a_index += 1
        index_count += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    # split array evenly as possible
    # do this recursivly until a single element is left
    mid = len(arr) // 2
    arrA = merge_sort(arr[0:mid])
    arrB = merge_sort(arr[mid:])

    # when at a single element merge

    return merge(arrA, arrB)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
