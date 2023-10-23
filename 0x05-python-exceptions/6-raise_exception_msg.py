#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raises a name exception with a message.

    :param message: exception message, defaults to ""
    :type message: str, optional
    :raise NameError: Always raise NameError with `message` as argument
    """
    raise NameError(message)
