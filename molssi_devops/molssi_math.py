"""
molssi_math.py
A package containing useful math functions

Handles the primary functions
"""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def mean(my_list):
    """
  
    Compute the mean of a list
 
    Parameters
    ----------
    my_list : list, default: True
        The list of numbers of which we want the mean

    Returns
    -------
    mean_list : float
        The mean of the list

    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    if not isinstance(my_list, list):
        raise TypeError("Mean '%s' is not a list" % my_list)

    if len(my_list) == 0:
        raise ZeroDivisionError("The input list has no elements")

    return sum(my_list) / len(my_list)


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
