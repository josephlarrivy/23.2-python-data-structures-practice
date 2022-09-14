def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # my work
    set1 = set(l1)
    set2 = set(l2)
    set_intersect = set1 & set2
    new_list = list(set_intersect)
    return new_list

    # solution
    # set2 = set(l2)
    # return[val for val in l1 if val in set2]