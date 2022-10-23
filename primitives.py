from math import hypot

class Point:
    def __init__(self,x,y,label=None):
        self.x = x
        self.y = y
        self.label = label
    def __eq__(self,other):
        if(self.x == other.x and self.y == other.y):
            return True
        return False
    def dbg(self,a=""):
        print("Point: ",a," X ",self.x," Y ",self.y)


def signedArea(p1, p2, p3):
    return (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)

def ccw(p1,p2,p3):
    return signedArea(p1,p2,p3) > 0

def dotProduct(p,q):
    return (p.x * q.x + p.y * q.y) 

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

def distP2P(p1,p2):
    return hypot(p1.y - p2.y, p1.x - p2.x)

def distP2L(p1,p2,q2):
    return 2 * abs(signedArea(p1,p2,q2)) / distP2P(p2,q2)

def perpendicularLine(p1,p2,q2):
    print(p2.x,p2.y)
    print(q2.x,q2.y)
    a2 = q2.y - p2.y
    b2 = -(q2.x - p2.x)
    a1 = -b2
    b1 = a2
    c1 = -(p1.x*a1 + p1.y*b1)
    print("a: ",a1,"b: ", b1, "c: ", c1)
    if(a1 != 0): 
        xAns = -(c1)/a1
        return Point(xAns,0)
    yAns = -(c1)/b1
    return Point(0,yAns)

def IntersecPoint(p1,q1,p2,q2):
    a1 = p1.y - q1.y
    b1 = p1.x - q1.x
    c1 = (p1.x*a1 + b1*p1.y)

    a2 = p2.y - q2.y
    b2 = p2.x - q2.x
    c2 = (p2.x*a2 + b2*p2.y)

    det = a1*b2 - a2*b1
    print("DET: ", det)
    if(det == 0):
        return None
    x = (b2*c1 - b1*c2)/det
    y = (a1*c2 - a2*c1)/det
    return Point(x,y)

def IntersectionOnSegment(a,b,p):
        AB = Point(b.x-a.x,b.y-a.y)
        BP = Point(p.x-b.x,p.y-b.y)
        AP = Point(p.x-a.x,p.y-a.y)

        AB_BP = dotProduct(AB,BP)
        AB_AP = dotProduct(AB,AP)
        ans = 0

        if(AB_BP > 0):
            ans = b
        elif(AB_AP < 0):
            ans = a
        else:
            perpendicularLinePoint = perpendicularLine(a,p,b)
            ans = IntersecPoint(perpendicularLinePoint,p,a,b)
        return ans
    
def isAbove(p1,q1,p2):
    return signedArea(p1,q1,p2) > 0

















