from attr import NOTHING
from convex_hull import *
from primitives import *
from math import *

class Classifier:
    def __init__(self,ch1,ch2):
        self.ch1 = ch1
        self.ch2 = ch2
    def separatingAxis(self):
        cv1 = self.ch1
        cv2 = self.ch2
        dist = float('inf')
        for pt1 in cv1.hull:
            for pt2 in cv2.hull:
                actual_distance = distP2P(pt1,pt2)
                if(actual_distance < dist):
                    dist = actual_distance
                    r = pt1
                    s = pt2
        mid_point = Point((r.x+s.x)/2,(r.y+s.y)/2)
        self.p,self.q = mid_point, perpendicularLine(mid_point,r,s)
        if(isAbove(self.p,self.q,r)):
            self.label1 = cv1.label
            self.label2 = cv2.label
        else:
            self.label1 = cv2.label
            self.label2 = cv1.label
    def classify(self,pt):
        if(isAbove(self.p,self.q,pt)):
            print(self.label1)
        else:
             print(self.label2)
    
    



