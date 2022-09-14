def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # my work
    new_list = []
    non_true_elements = [0, 0.0,'',None,False,[],{},()]
    for item in lst:
        if (item not in non_true_elements):
            new_list.append(item)
    return new_list

    # solution:
    # return [val for val in lst if val]