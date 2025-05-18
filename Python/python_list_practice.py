"""
Interchange the first and last elements in a list
"""
def swap_first_last_element(lst):
    fst = lst[0]
    lst[0] = lst[-1]
    lst[-1] = fst
    #can be condensed into lst[0],lst[-1] = lst[-1], lst[0]
    return lst

"""
Swap two elements in a list
"""
def swap_elements(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return lst

if __name__ == '__main__':
    lst = ['a','b','c','d','e']
    #print(swap_first_last_element(lst))
    print(swap_elements(lst, 1, 4))