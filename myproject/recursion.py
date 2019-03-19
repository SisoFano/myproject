def sum_array(array):
    """Return sum of all items in array.

    Args:
        items (array): list or array-like object containing numerical values.

    Returns:
        sum: sum of elements in array.

    Examples:
        >>> sum_array([8, 7, 3])
        18
    """
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    """Return n!.

    Args:
        n (int): calculates factorial of nth term.

    Returns:
        int: factorial

    Examples:
        >>> factorial(1)
        1
        >> factorial(2)
        2
        >> factorial(3)
        6
    """
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):

    """Return word in reverse.

    Args:
        word: a string

    Returns:
        str: word in reverse

    Examples:
        >>> reverse('word')
        'drow'
    """
    if word == '':
        return word
    else:
        return word[-1] + reverse(word[:-1])
