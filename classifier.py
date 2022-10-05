from attr import NOTHING
from convex_hull import *
from primitives import *
from math import *

class Classifier:
    def __init__(self,train):
        NOTHING
    def ClosestSegment(a,b,p):
        AB = (b.x-a.x,b.y-a.y)
        BP = (p.x-b.x,p.y-b.y)
        AP = (p.x-a.x,p.y-a.y)

        AB_BP = dotProduct(AB,BP)
        AB_AP = dotProduct(AB,AP)
        ans = 0

        if(AB_BP > 0):
            x = p.x - b.x
            y = p.y - b.y
            ans = (hypot(x,y),p,b)
        elif(AB_AP < 0):
            x = p.x - a.x
            y = p.y - a.y
            ans = (hypot(x,y),p,a)
        else:
            mod = hypot(AB.x,AB.y)
            dist = abs(AB.x * AP.y - AB.y * AP.x)/mod
            ans = (dist,p,None)
