# done
def weekday_name(day_of_week):
    if day_of_week < 1 or day_of_week > 7:
        return None
    else:
        return days[day_of_week]

days = {
    1:'sunday',
    2:'monday',
    3:'tuesday',
    4:'wednesday',
    5:'thursday',
    6:'friday',
    7:'saturday'
}






"""Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """