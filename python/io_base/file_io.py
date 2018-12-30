def save_line(line, filename):
    """Save a line of text.
    Args:
        line (str): Text.
        filename (str): Name of the file.
    Examples:
        >>> save_line("hello world!", "file.txt")
    """
    with open(filename, "w") as f:
        f.write(line)


def read_line(filename):
    """Read a line of text.
    Args:
        filename (str): Name of the file.
    Returns:
        str: Text.
    Examples:
        >>> read_line("share/data1.txt")
        'I like to move it, move it'
    """
    with open(filename, "r") as f:
        txt = f.readline()
    return txt


def save_list(alist, filename):
    pass


def load_list(filename):
    pass
