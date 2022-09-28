

from numpy import true_divide

eps = 1e-9

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def signedArea(p1, p2, p3):
    return (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)

def orientation(p1,p2,p3):
    sArea = signedArea(p1,p2,p3)
    if(sArea == 0):
        return 0
    if(sArea < 0):
        return 2
    return 1

def isOnSegment(p1,p2,p3):
    if(p2.x <= max(p1.x,p3.x) and p2.x >= min(p1.x, p3.x) and p2.y <= max(p1.y, p3.y) and p2.y >= min(p1.y,p3.y)):
        return True
    return False

def doIntersect(p1,q1,p2,q2):
    o1 = orientation(p1,q1,p2)
    o2 = orientation(p1,q1,q2)
    o3 = orientation(p2,q2,p1)
    o4 = orientation(p2,q2,q1)

    if(o1 != o2 and o3 != o4):
        return True

    if(o1 == 0 and isOnSegment(p1,p2,q1)):
        return True
    if(o2 == 0 and isOnSegment(p1,q2,q1)):
        return True
    if(o3 == 0 and isOnSegment(p2,p1,q2)):
        return True
    if(o4 == 0 and isOnSegment(p2,q1,q2)):
        return True
    
    return False


def floatEq(f1,f2):
    abs(f1 - f2) <= eps

def floatLt(f1,f2):
    (f2 - f1) > eps





