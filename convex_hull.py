
from more_itertools import first_true
from primitives import *

class Convex_hull:
    def __init__ (self,points,label=""):
        self.label = label
        self.all_points = points
        self.hull = []

        sz = len(points)
        if(sz < 3):
            print("Para criar o envoltório convexo é necessário pelo menos 3 pontos.")
            return
        leftIndex = 0
        for i in range(sz):
            if(points[i].x < points[leftIndex].x  or (points[i].x == points[leftIndex].x and points[i].y < points[leftIndex].y)):
                leftIndex = i
        
        p1 = leftIndex
        while True:
            self.hull.append(points[p1])
            p2 = (p1+1)%sz
            for i in range(sz):
                o = orientation(points[p1],points[i],points[p2])
                
                if o == 2 or (o == 0 and distP2P(points[p1],points[i]) > distP2P(points[p1],points[p2])):
                #if o == 2:
                    print("Pi: ",distP2P(points[p1],points[i]))
                    print("P2: ",distP2P(points[p1],points[p2]))
                    p2 = i
            p1 = p2
            if(p1 == leftIndex):
                break


        """ n = len(points)
        print("N",n)
        if(n < 3):
            print("Para criar o envoltório convexo é necessário pelo menos 3 pontos.")
            return

        points.sort()
        aux = []
        for i in range(n):
            m = len(self.hull)
            while(m > 1 and not ccw(self.hull[m-2],self.hull[m-1],points[i])):
                self.hull.pop()
                m = len(self.hull)
            self.hull.append(points[i])
        for i in reversed(range(n)):
            m = len(aux)
            while(m > 1 and not ccw(aux[m-2], aux[m-1],points[i])):
                aux.pop()
                m = len(aux)
            aux.append(points[i])
        self.hull.pop(len(self.hull)-1)
        aux.pop(len(aux)-1)
        for pt in aux:
            self.hull.append(pt) """

            



    
    def isInside(self, q):
        for pt in self.hull:
            if pt == q:
                return True
        auxHull = []
        auxHull = self.hull.copy()
        auxHull.append(q)
        print("LEN",len(auxHull))
        chAux = Convex_hull(auxHull,"")
        print("AQUI")
        for pt in chAux.hull:
            if pt.x == q.x and pt.y == q.y:
                return False
        return True
            
        """ ptINF = Point(int(1e9),pt.y)
        sz = len(self.hull)
        count = 0
        i = 0
        while True:
            intercpts = []
            j = (i+1)%sz
            if(self.hull[i].y == pt.y):
                count -= 1
            if(doIntersect(self.hull[i],self.hull[j],pt,ptINF)):
                intercpts.append((self.hull[i],self.hull[j]))
                if(orientation(self.hull[i],pt,self.hull[j]) == 0):
                    return isOnSegment(self.hull[i],pt,self.hull[j])
                count += 1
            i = j
            if(i == 0):
                break
            if(not count%2):
                for elm in intercpts:
                    print("P:",elm[0].x,elm[0].y)
                    print("Q:",elm[1].x,elm[1].y)
        return (count%2 == 1) """

def areIndependent(ch1, ch2):
    for pt in ch1.hull:
        print(pt.x,pt.y)
        if(ch2.isInside(pt)):
            print(pt.x,pt.y)
            return False
    for pt in ch2.hull:
        print(pt.x,pt.y)
        if(ch1.isInside(pt)):
            print(pt.x,pt.y)
            return False
    return True
        