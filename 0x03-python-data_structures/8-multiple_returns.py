#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the length of a string
    and its first character.

    Args:
    sentence (str): string

    Returns:
    (tuple)

    If the sentence is empty, the first character should be equal to `None`.

    Examples:
    >>> sentence = "At school, I learnt C!"
    >>> length, first = multiple_returns(sentence)
    >>> print("Length: {:d} - First character: {}".format(length, first))
    Length: 22 - First character: A
    """
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
