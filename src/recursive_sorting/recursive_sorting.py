# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    #we start at the first element of each array
    #we also will first append to the 0th index of the merged_arr array
    arrA_index = 0
    arrB_index = 0
    merged_arr_index = 0

    #while there are still values to index on each the left and right array...
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        #if the value in arrayA is smaller...
        if arrA[arrA_index] <= arrB[arrB_index]:
            #append the next value in arrA to the merged_arr array
            merged_arr[merged_arr_index] = arrA[arrA_index]
            #incriment the merged array and A array index
            arrA_index += 1
        else:
            #append the next value in arrB to the merged_arr array
            merged_arr[merged_arr_index] = arrB[arrB_index]
            #incriment the merged array and the B array index
            arrB_index += 1
        
        merged_arr_index +=1
        
    while arrB_index < len(arrB):
        #we have gone through all of the A array values...
        #we need to add the final B array value to the merged_arr_index
        merged_arr[merged_arr_index] = arrB[arrB_index]
        arrB_index += 1
        merged_arr_index += 1
    while arrA_index < len(arrA):
        #we have gone through all of the A array values...
        #we need to add the final B array value to the merged_arr_index
        merged_arr[merged_arr_index] = arrA[arrA_index]
        arrA_index += 1
        merged_arr_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    else:
    
        while True:
            split_index = len(arr) // 2
            left_list = merge_sort(arr[:split_index])
            right_list = merge_sort(arr[split_index:])
            return merge(left_list,right_list)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO


    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
