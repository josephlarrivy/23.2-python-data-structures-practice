def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # new_dict = {}.fromkeys(phrase, 0)
    # return new_dict

    # letter_dict = {letter: 'x' for letter in phrase}
    # return letter_dict

    letter_dict = {}
    for letter in phrase:
        letter_dict[letter] = letter_dict.get(letter, 0) +1

    return letter_dict