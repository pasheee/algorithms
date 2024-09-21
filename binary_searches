def lbs(mass, elem):
    l = -1
    r = len(mass) - 1
    while l+1 < r:
        m = (l+r)//2
        if mass[m] < elem:
            l = m
        else:
            r = m
    return r
    
def rbs(mass, elem):
    l = 0
    r = len(mass)
    while l + 1 < r:
        m = (l+r)//2
        if mass[m] > elem:
            r = m
        else:
            l = m
    return l
