

#Selection sort
"""Whe should get the first position and compare to the next an see if they're a minus value, 
if true change the position of the element and pass to the next position"""
def selection_sort(list):
    length_list = len(list) #the lenght of the list

    for pointer_index in range(length_list - 1): #for to define the main pointer, We don't need to pass trought the last value
        min_index = pointer_index #minor value to the turn

        for member_index in range(pointer_index + 1, length_list): #for to pass for each value from pointer until list lenght, we start to the next valeu of point 
            if list[member_index] < list[min_index]: #to compare if the actual position from the pointer is bigger than the next position
                min_index = member_index #assign index to the min_index

        if list[pointer_index] > list[min_index]:#change values according to index
            actual_pointer_value = list[pointer_index] #save the value that are going to be changed to not lose it
            list[pointer_index] = list[min_index] #change the pointer value to the minor value 
            list[min_index] = actual_pointer_value #change the value of the old minor position receinvg the pointer has changed 

        print(list)
    print(list)

#Buble sort
"""We should form pairs in elements that are in position consecutives. We proceed to the next positions comparing the minor first value from the pair"""
def bubble_sort(list):
    length_list= len(list) #gets the size of the list
    for pointer in range(length_list - 1):# pass through the lisst, we don't need the last element because we are going to compare the penult to the last one 
        for actual_member_index in range(length_list - 1):
            if list[actual_member_index] > list[actual_member_index + 1]: #if the element is bigger than your next one
                list[actual_member_index], list[actual_member_index + 1] = list[actual_member_index + 1], list[actual_member_index] #change their position

    print(list)
            
#Insertion sort
"""We should compare the second element disorgonized to the the group organized, starting from the last one"""
def insertion_sort(list):
    length_list = len(list)
    for member_index in range(1,length_list): #we start with the second value because we considered the first one an organized group
        pointer_index = member_index - 1 #declare a before position of the organized group
        key = list[member_index] #save the actual position to organize
        
        while pointer_index >= 0 and list[pointer_index] > key: #while the pointer isn't the first and their value is bigger than key
            list[pointer_index + 1]= list[pointer_index] #the next value from the pointer receive the pointer value
            pointer_index -= 1 #the pointer draw back to the penult values
        
        list[pointer_index + 1] = key #put the key in the right place,one position before pointer receive the key considering it is bigger
    print(list)

#Merge sort
"""We compare each value after separate individually by the midle in mini lists, after separate we get the list previous and organize it"""
def merge_sort(list,start=0,end=None):#responsable to separate each element 
    
    if end is None:
        end = len(list)

    if(end - start > 1): #define if the value is separated in an unique way
        midle = (end + start)//2 #integer division
        merge_sort(list, start, midle) #get the first part of the list
        merge_sort(list, midle, end)#get the second part of the list
        merge(list, start, midle, end)

def merge(list, start, midle, end):# ordenate and join the list
    left_list = list[start:midle] #left elements
    right_list= list[midle:end] #right elements
    top_right,top_left= 0, 0 #value of top of each list
    for index in range(start, end):#pass through the list
        if top_left >= len(left_list):#if  the top index is bigger or the same value from the list length
            list[index] = right_list[top_right] #put the right value in that position
            top_right = top_right + 1#the top index proceed ot the next one
        elif top_right >= len(right_list):#if the right index is bigger or the same value from the list length
            list[index] = left_list[top_left]
            top_left = top_left + 1#the top index proceed ot the next one
        elif left_list[top_left] < right_list[top_right]: #if the top in the list left is minor than right list
            list[index] = left_list[top_left]#the turn value receive the left top value
            top_left = top_left + 1 # the top index proceed to the next value
        else: #the right list is minor
            list[index] = right_list[top_right] #the turn value receive the right top value
            top_right = top_right + 1 #the top index proceed ot the next one
            


#Quicksort
"""We separate the minor value of pivot in a list, passing trough that list again to organize"""
def quicksort(list, start=0, end=None):#responsable to do the recursion to pass on partition 
    if end is None: # If it is the first execution
        end = len(list) - 1 #define the end index, removing the last on considering the pivot
    if start < end: #if there is more than one element
        pivot = partition(list,start,end) #separate the values in partitions
        quicksort(list, start, pivot - 1) #left sublist 
        quicksort(list, pivot + 1, end) #right sublist

def partition(list,start,end): 
    pivot = list[end] #always being the last element
    minor_values_index = start #always start being in the first position
    for bigger_value_index in range(start, end): #The loop to pass for each element 
        if list[bigger_value_index] <= pivot: #compare the pivot to each position
            list[bigger_value_index], list[minor_values_index] = list[minor_values_index], list[bigger_value_index] #turn their positions
            minor_values_index = minor_values_index + 1 #proceed according to the progression of minor quantity values
    list[minor_values_index], list[end] = list[end], list[minor_values_index] #turn their values
    return minor_values_index
list = [9,4,2,8,6,1,3,5]
quicksort(list)
print(list)