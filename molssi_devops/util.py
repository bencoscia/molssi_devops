"""
util.py
A sample repository for the MolSSI Python package development workshop

Misc. utility functions
"""


def title_case(sentence):
    """
    Convert a string into title case.

    Title case means that the first letter of each word is capitalized, and all other letters in the word are lowercase.

    Parameters
    ----------
    sentence: str
        String to be converted to title case.

    Returns
    -------
    ret: str
        String converted to title case.

    Example
    -------
    >>> title_case('ThIS is a STRinG to BE ConVerTeD.')
    'This Is A String To Be Converted.'
    """

    words = sentence.split()
    title = ""
    for word in words:
        title += word[0].upper() + word[1:].lower() + " "
    return title




