def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while n >= 1:
        if n % 10 == 8:
            i += 1
        else:
            i = 0
        while i == 2:
            return True
        n = n // 10
    return False
    
print(double_eights(29784889328547))