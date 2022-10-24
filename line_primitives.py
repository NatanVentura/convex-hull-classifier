# Primitivas geométricas envolvendo linhas e segmentos

from point_primitives import *

# Dado um ponto p2 colinear ao segmento p1 p3, retorna verdadeiro se esse
# ponto pertence ao segmento 
def isOnSegment(p1,p2,p3):
    if(p2.x <= max(p1.x,p3.x) and p2.x >= min(p1.x, p3.x) and p2.y <= max(p1.y, p3.y) and p2.y >= min(p1.y,p3.y)):
        return True
    return False

# Recebe 2 segmentos p1 q1 e p2 q2
# Retorna verdadeiro se eles se interctam
def doIntersect(p1,q1,p2,q2):

    # Orientação entre cada tripla de pontos
    o1 = orientation(p1,q1,p2)
    o2 = orientation(p1,q1,q2)
    o3 = orientation(p2,q2,p1)
    o4 = orientation(p2,q2,q1)

    # Caso normal, se as direções divergem então há interceptação 
    if(o1 != o2 and o3 != o4):
        return True

    # Caso de canto, caso sejam colineares
    # verifica-se se o ponto colinear pertence ao segmento
    if(o1 == 0 and isOnSegment(p1,p2,q1)):
        return True
    if(o2 == 0 and isOnSegment(p1,q2,q1)):
        return True
    if(o3 == 0 and isOnSegment(p2,p1,q2)):
        return True
    if(o4 == 0 and isOnSegment(p2,q1,q2)):
        return True
    
    # Retorna falso caso não esteja em nenhum dos casos anteriores
    return False




# Recebe um ponto (p1) e uma reta (p2,q2)
# Retorna um ponto pertencente a reta perpendicular à reta (p2,q2)
# que passa pelo ponto (p1)
def perpendicularLine(p1,p2,q2):

    # coeficientes lineares da reta p2,q2
    a2 = q2.y - p2.y
    b2 = -(q2.x - p2.x)

    # coeficientes da reta perpendicular que passa por p1
    a1 = -b2
    b1 = a2
    c1 = -(p1.x*a1 + p1.y*b1)

    # Caso a diferente de 0, retornamos o ponto da reta que passa por y = 0
    # pois não pode haver divisão por 0
    if(a1 != 0): 
        xAns = -(c1)/a1
        return Point(xAns,0)
    
    # senão, retornamos o ponto pertencente a reta que passa por x = 0
    yAns = -(c1)/b1
    return Point(0,yAns)

# Recebe uma linha (p1,q1) e o ponto p2
# Retorna verdadeito se o ponto está no sentido horário da linha    
def ccw(p1,q1,p2):
    return signedArea(p1,q1,p2) > 0

















