"""Return the index from a element if it is in the list"""
def basic_search(list, element): #log(n) / Linear Search
    for i in range(len(list)):
        if list[i] == element:
            return i
            
    return None