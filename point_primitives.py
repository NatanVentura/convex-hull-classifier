
from math import hypot

# Objeto com atributos x,y e um atributo opcional label
class Point:

    # Construtor
    def __init__(self,x,y,label=None):
        self.x = x
        self.y = y
        self.label = label

    # Implementação do operador '=' para o ponto
    # Dois pontos são iguais se possuem x e y iguais
    # O atributo label não é levado em consideração
    def __eq__(self,other):
        if(self.x == other.x and self.y == other.y):
            return True
        return False

# Recebe 3 pontos e retorna o cross product deles
def signedArea(p1, p2, p3):
    return (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)

# Recebe dois pontos e retorna a distância entre eles
def dist(p1,p2):
    return hypot(p1.y - p2.y, p1.x - p2.x)

# Retorna orientação de três pontos
# 0 se colineares
# 1 se no sentido horário
# 2 se no sentido anti horário
def orientation(p1,p2,p3):
    sArea = signedArea(p1,p2,p3)
    if(sArea == 0):
        return 0
    if(sArea < 0):
        return 2
    return 1