

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
        print(list)
    print(list)
            
