def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # my work
    new_phrase = phrase.replace(phrase[0], phrase[0].upper())
    return new_phrase 

    # solution
    # return phrase.capitalize()