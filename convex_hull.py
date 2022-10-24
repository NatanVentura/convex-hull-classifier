
from line_primitives import *
from point_primitives import *

# Classe do Envoltório convexo
# Como atributos tem uma label indicando a classe,
# todos os pontos pertencentes ao poligono e os pontos do envoltório
class Convex_hull:

    # Construtor, recebe os pontos e uma label indicando a classe (opcional)
    # Não tem retorno, mas guarda os pontos do envoltório no atributo hull
    # Implementação do algoritmo de Jarvis devido sua facilidade de tratar pontos colineares
    def __init__ (self,points,label=""):

        # Atributos
        self.label = label
        self.all_points = points
        self.hull = []

        # Se o número de pontos é menor que 3 dispara uma exceção
        sz = len(points)
        if(sz < 3):
            raise Exception("It's necessary at least 3 points to create convex hull.")
        
        # Define o ponto incial como o ponto mais à esquerda 
        start = 0
        for i in range(sz):
            if(points[i].x < points[start].x  or (points[i].x == points[start].x and points[i].y < points[start].y)):
                start = i
        
        #definimos o ponto anterior como o inicio
        prev = start

        while True:
            # O ponto anterior é adicionado no envoltório
            self.hull.append(points[prev])

            # Definimos o próximo ponto, inicialmente como um ponto depois do ponto atual
            nxt = (prev+1)%sz

            # Iteração por todos os pontos
            for i in range(sz):
                # Orientação entre o ponto anterior, o ponto atual e o próximo ponto
                o = orientation(points[prev],points[i],points[nxt])

                # Caso o ponto esteja no sentido anti-horário 
                # ou seja colinear e mais distante que o ponto atual
                # então mudamos o próximo ponto para ser o ponto i atual
                if o == 2 or (o == 0 and dist(points[prev],points[i]) > dist(points[prev],points[nxt])):
                    nxt = i
            
            # Caso o próximo ponto seja igual ao ínicio, encerramos o loop
            if(nxt == start):
                break

            # O anterior é definido como o próximo e o loop ocorre novamente
            prev = nxt
    
    # Recebe um ponto q e retorna verdadeiro se o ponto está dentro do envoltório
    def isInside(self, q):

        # Caso o ponto q esteja no exterior do envoltório, retorna verdadeiro
        for i in range(len(self.hull)):
            j = (i+1)%len(self.hull)

            #Se for colinear com as retas do envoltório e estiver no segmento então retornamos verdadeiro
            if(orientation(self.hull[i],self.hull[j],q) == 0 and isOnSegment(self.hull[i],q,self.hull[j])):
                return True
        
        # Criaremos um envoltório auxiliar,
        # nesse envoltório teremos os pontos do envoltório anterior e o ponto q,
        # Caso qesteja fora do envoltório os pontos do envoltório auxiliar terão q no enoltório
        # Caso contrário, o ponto está dentro do envoltório
        auxHull = []
        auxHull = self.hull.copy()
        auxHull.append(q)
        chAux = Convex_hull(auxHull,"")
        for pt in chAux.hull:
            if pt.x == q.x and pt.y == q.y:
                return False
        return True

#Dados dois envoltórios (ch1 e ch2)
# Retornamos verdadeiro se eles são linearmente independentes
def areIndependent(ch1, ch2):

    # para cada ponto do envoltorio ch1 verificamos se ele está em ch2 e vice-versa
    for pt in ch1.hull:
        if(ch2.isInside(pt)):
            return False
    for pt in ch2.hull:
        if(ch1.isInside(pt)):
            return False
    return True
        