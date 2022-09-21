

def my_funct():
    """
    function declare dictionary again
    :return: Dictionary
    """
    l = [('1', 2), ('3', 4)]
    d = dict()
    for k, v in l:
        d[k] = v
        return d
