def maxDivision(former, latter):
    ret = 1
    end = min(former, latter)
    for i in range(1, end + 1):
        if (former % i == 0 and latter % i == 0):
            ret = i
    return ret
