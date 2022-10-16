from attr import NOTHING
from convex_hull import *
from primitives import *
from sklearn.metrics import *
from math import *

class Classifier:
    def __init__(self,points1,points2,l1,l2):
        self.l1 = l1
        self.l2 = l2
        self.trueL1 = 0
        self.trueL2 = 0
        self.falseL1 = 0
        self.falseL2 = 0
        self.total = 0
        self.ch1 = Convex_hull(points1,l1)
        self.ch2 = Convex_hull(points2,l2)
        self.hasClassifier = areIndependent(self.ch1,self.ch2)
        if(self.hasClassifier):
            self.separatingAxis()
        else:
            print("Nao foi possivel criar o classificador, os dados nao sao independentes.")
    def separatingAxis(self):
        cv1 = self.ch1
        cv2 = self.ch2
        dist = float('inf')
        for pt1 in cv1.hull:
            for pt2 in cv2.hull:
                actual_distance = distP2P(pt1,pt2)
                if(actual_distance < dist):
                    dist = actual_distance
                    self.r = pt1
                    self.s = pt2
        mid_point = Point((self.r.x+self.s.x)/2,(self.r.y+self.s.y)/2)
        self.p,self.q = mid_point, perpendicularLine(mid_point,self.r,self.s)
        if(isAbove(self.p,self.q,self.r)):
            self.label1 = cv1.label
            self.label2 = cv2.label
        else:
            self.label1 = cv2.label
            self.label2 = cv1.label
    def classify(self,pt):
        if(self.hasClassifier == False):
            print("Impossivel classificar, classificador nao foi criado")
            return
        self.total += 1
        if(isAbove(self.p,self.q,pt)):
            if(pt.label == self.l1):
                self.trueL1 += 1
            else:
                self.falseL1 += 1
        else:
            if(pt.label == self.l2):
                self.trueL2 += 1
            else:
                print(pt.x,pt.y,pt.label)
                self.falseL2 += 1
    def printMetrics(self):
        precision = self.trueL1/(self.trueL1+self.falseL1)
        recall = self.trueL1/(self.trueL1+self.falseL2)
        fscore = 2*(precision*recall)/(precision+recall)
        accuracy = (self.trueL1+self.trueL2)/self.total
        print('Precisao: ',precision)
        print('Recall', recall)
        print('F1: ',fscore)
        print('Accuracy: ',accuracy)

    
    



