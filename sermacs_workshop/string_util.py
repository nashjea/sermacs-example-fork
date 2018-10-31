"""
Some misc string functions

Workshop @ SERMACS
"""

def title_case(sentence):
    """
    Convert a string to title case

    Title case means that the first character of every word is capitalized, otherwise,
    lowercase.

    Parameters
    ------------------
    sentence: string
        The string to convert to title title case

    Returns
    ------------------
    str
        The input string in title case

    Examples
    --------------------
    >>> title_string("thIs iS a StrIng to bE CONverTed")
    'This Is A String To Be Converted'
    """

    ret = sentence[0].upper()

    for i in range(1, len(sentence)):
        if sentence[i - 1] == '':
            ret += sentence[i].upper()
        else:
            ret += sentence[i].lower()
    return ret
