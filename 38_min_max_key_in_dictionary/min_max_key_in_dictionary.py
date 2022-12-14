def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    # my work
    
    # keys = set(d.keys())
    # keys_list = [*keys]
    # print(keys_list)
    # length = len(keys_list)-1
    # tup = (keys_list[0],keys_list[length])
    # print(tup)

    # solution
    keys = d.keys()
    return (min(keys), max(keys))