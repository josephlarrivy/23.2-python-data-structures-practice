# done
def last_element(lst):
    length  = len(lst)
    lst.pop(length -1)



def last_element_solution(lst):
    if lst:
        return lst[-1]



"""Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """