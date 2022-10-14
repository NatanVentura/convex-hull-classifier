
from primitives import *

class Convex_hull:
    def __init__ (self,points):
        self.hull = []
        sz = len(points)
        if(sz < 3):
            print("Para criar o envoltório convexo é necessário pelo menos 3 pontos.")
            return
        leftIndex = 0
        for i in range(sz):
            if(points[i].x < points[leftIndex].x):
                leftIndex = i
        
        p1 = leftIndex
        while True:
            self.hull.append(points[p1])
            p2 = (p1+1)%sz
            for i in range(sz):
                if(orientation(points[p1],points[i],points[p2]) == 2):
                    p2 = i
            p1 = p2
            if(p1 == leftIndex):
                break
    def isInside(self, pt):
        ptINF = Point(int(1e9),pt.y)
        sz = len(self.hull)
        count = 0
        i = 0
        while True:
            j = (i+1)%sz
            if(self.hull[i] == pt.y):
                count -= 1
            if(doIntersect(self.hull[i],self.hull[j],pt,ptINF)):
                if(orientation(self.hull[i],pt,self.hull[j]) == 0):
                    return isOnSegment(self.hull[i],pt,self.hull[j])
                count += 1
            i = j
            if(i == 0):
                break
        return (count%2 == 1)

def areIndependent(ch1, ch2):
    n = len(ch1.hull)
    m = len(ch2.hull)
    for i1 in range(n):
        j1 = (i1+1)%n
        for i2 in range(m):
            j2 = (i2+1)%m
            if(doIntersect(ch1.hull[i1],ch1.hull[j1],ch2.hull[i2],ch2.hull[j2])):
                return False
    return True
def separatingAxis(cv1,cv2):
    dist = float('inf')
    for pt1 in cv1.hull:
        for pt2 in cv2.hull:
            actual_distance = distP2P(pt1,pt2)

            if(actual_distance < dist):
                dist = actual_distance
                r = pt1
                s = pt2
    mid_point = Point((r.x+s.x)/2,(r.y+s.y)/2)
    return r,s, mid_point, perpendicularLine(mid_point,r,s)
        