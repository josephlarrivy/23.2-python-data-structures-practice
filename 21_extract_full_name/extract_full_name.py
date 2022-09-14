people = [
             {'first': 'Ada', 'last': 'Lovelace'},
             {'first': 'Grace', 'last': 'Hopper'},
            ]


def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> people = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    # my work
    # full_names_list = []
    # for person in people:
    #     first = person['first']
    #     last = person['last']
    #     full_names_list.append(f'{first} {last}')
    #     # full_names_list.append(last)
    # return full_names_list

    # solution
    return [f"{person['first']} {person['last']}" for person in people]