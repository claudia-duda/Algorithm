#Selection sort
"""Whe should get the first position and compare to the next an see if they're a minus value, 
if true change the position of the element and pass to the next position"""

list = [9,4,2,8,6,1,3,5] #gets the list
length_list = len(list) #the lenght of the list

for pointer_index in range(length_list - 1): #for to define the main pointer, We don't need to pass trought the last value
    min_index = pointer_index #minor value to the turn

    for member in range(pointer_index + 1, length_list): #for to pass for each value from pointer until list lenght, we start to the next valeu of point 
        if list[member] < list[min_index]: #to compare if the actual position from the pointer is bigger than the next position
            min_index = member #assign index to the min_index

    if list[pointer_index] > list[min_index]:#change values according to index
        actual_pointer_value = list[pointer_index] #save the value that are going to be changed to not lose it
        list[pointer_index] = list[min_index] #change the pointer value to the minor value 
        list[min_index] = actual_pointer_value #change the value of the old minor position receinvg the pointer has changed 
        
    print(list)
print(list)