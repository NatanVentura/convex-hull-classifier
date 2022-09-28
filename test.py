
from convex_hull import Convex_hull, areIndependent
from primitives import Point

points = [Point(0,0),Point(2,1),Point(2,5),Point(1,3),Point(1,2),Point(0,4)]
cv1 = Convex_hull(points)
for elm in cv1.hull:
    print("X: ", elm.x, "|| Y: ",elm.y)

points = [Point(10,10),Point(-1,-1),Point(1,3),Point(0,4),Point(1,4.6),Point(1,2)]
for elm in points:
    print("X: ", elm.x, "|| Y: ",elm.y, "|| Tá dentro: ",cv1.isInside(elm))


print()
print()
print()

cv2 = Convex_hull([Point(1,3),Point(3,3),Point(3,4)])
cv3 = Convex_hull([Point(0,0),Point(0,-1),Point(1,0)])
cv4 = Convex_hull([Point(0,6),Point(2,6),Point(0,7)])
cv5 = Convex_hull([Point(-1,-1),Point(3,-1),Point(3,-2)])

cvs = [cv2,cv3,cv4,cv5]

for cv in cvs:
    print(areIndependent(cv1,cv))
