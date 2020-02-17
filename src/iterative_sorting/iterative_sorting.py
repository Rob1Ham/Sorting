# TO-DO: Complete the selection_sort() function below 

import random

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]
arr4 = random.sample(range(200), 50)


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(smallest_index+1,len(arr)):
            if arr[j] <= arr[smallest_index]:
                old_low = arr[smallest_index]
                new_low = arr[j]
                arr[smallest_index] = new_low
                arr[j] = old_low
        
        # TO-DO: swap
        arr[i] = arr[smallest_index]
    return arr

# print(selection_sort(arr1))
# print(selection_sort(arr2))
# print(selection_sort(arr3))



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    bubbled = True
    if len(arr) <= 1:
        #can't sort a list of length 0 or 1
        bubbled = False
    while bubbled:
        #since its a new pass, the status of "new_order" is false
        new_order= False
        for n in range(0,len(arr)-1):
            #walk through the list across of values
            if arr[n] > arr[n+1]:
                #if the left side is bigger than the right side
                #their places are swapped
                bubble_up = arr[n]
                bubble_down = arr[n+1]
                arr[n] = bubble_down
                arr[n+1] = bubble_up
                #since a change occured, it has a new order
                new_order = True
            if new_order == True:
                #if there is a new order, do the process again
                bubbled = True
            else:
                #if no values are bubbled, break while loop and return sorted aray
                bubbled = False

    return arr


# print(bubble_sort(arr1))
# print(bubble_sort(arr2))
# print(bubble_sort(arr3))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1):

    #set max value in the array
    maximum = maximum
    #first check if negative, as negatives are not allowed in count sourt
    for i in range(len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
            
    
    #create count array of length the maximum value of the input array
    count_array = [0] * (maximum + 1)

    #walking across each value in the array, add that value to the count array
    for i in range(0, len(arr)):
        counter = arr[i]
        count_array[counter] += 1
    
    #import pdb; pdb.set_trace()
    #for each value in the count array, add the value of the previous element in the array
    for i in range(1,len(count_array)):
        count_array[i] = (count_array[i-1] + count_array[i])


    #import pdb; pdb.set_trace()
    #final array has same length as input array
    output_arr = [0] * len(arr)

    
   
    for i in range(0, len(arr)):
        #print("Index is" + str(i))
        count_index = arr[i]
        #print("countindex is: "+str(count_index))
        output_index= count_array[count_index]
        #print("output index is: "+str(output_index))
        count_array[count_index] -= 1
        #print("the value of" + str(count_index) + "is being placed at output index of: " + str(output_index))
        #print("New output array is: " + str(output_arr))
        output_arr[output_index-1] =  count_index
    
    arr = output_arr
    return arr

print(count_sort(arr1,10))
print(count_sort(arr2))
print(count_sort(arr3,5))
