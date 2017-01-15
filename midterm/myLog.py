def myLog(x, b):
    for i in range(x/2):
        if b**i==x:
            return i
        elif b**i<x and b**(i+1)>x:
            return i
        