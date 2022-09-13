# done
def reverse_string(phrase):
    phrase_list = list(phrase)
    phrase_list.reverse()
    reversed = ''.join(phrase_list)
    return reversed

def reverse_string_solution(phrase):
    return phrase[::-1]


    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
