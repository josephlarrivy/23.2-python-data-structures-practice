def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).
        >>> is_palindrome('tacocat')
        True
        >>> is_palindrome('noon')
        True
        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:
        >>> is_palindrome('taco cat')
        True
        >>> is_palindrome('Noon')
        True
    """
    phrase_list = list(phrase)
    phrase_list.reverse()
    reverse_list = phrase_list
    reverse_phrase = ''.join(reverse_list)
    reverse_lower = reverse_phrase.lower()
    phrase_lower = phrase.lower()
    if reverse_lower == phrase_lower:
        return True
    else:
        return False
