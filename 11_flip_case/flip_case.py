def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # if to_swap in 'abcdefghijklmnopqrstuvwxyz':
    #     print ('is lower')
    #     letter_upper = to_swap.upper()
    #     print(letter_upper)
    #     new_phrase = phrase.replace(to_swap, letter_upper)

    # elif to_swap in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    #     print ('is upper')
    #     letter_lower = to_swap.lower()
    #     new_phrase = phrase.replace(to_swap, letter_lower)

    
    # return new_phrase


    new_phrase = ''
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            letter = letter.swapcase()
            new_phrase += letter
            print(letter)
        else:
            new_phrase += letter
            print(letter)
    return new_phrase
