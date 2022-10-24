import warnings
from convex_hull import *
from line_primitives import *
from point_primitives import *

# Classe do classificador
# Dados os pontos e seus rótulos, ele cria dois envoltórios, um para cada rotúlo.
# Depois verifica se os dois envoltórios são linearmente independentes
# Caso sejam, cria um eixo que separa os dois envoltórios 
# Após a criação é possível classificar um novo dado como pertencente à uma das duas classe
# Por fim é possível imprimir as métricas de corretude do algoritmo para o conjunto de dados
class Classifier:

    # construtor, recebe como parametros os pontos da classe1, pontos da classe 2,
    # Rotúlo da classe 1 e rótulo da classe 2
    def __init__(self,points1,points2,l1,l2):

        # definição dos atributos
        self.trueL1 = 0
        self.trueL2 = 0
        self.falseL1 = 0
        self.falseL2 = 0
        self.total = 0

        # cria os envoltórios
        self.ch1 = Convex_hull(points1,l1)
        self.ch2 = Convex_hull(points2,l2)

        # Caso sejam independentes cria o eixo de separação
        self.hasClassifier = areIndependent(self.ch1,self.ch2)
        if(self.hasClassifier):
            self.separatingAxis()
        else:
            warnings.warn("Data are not independent, it's impossible to create classifier.")
    
    # Cria o eixo de separação dos envoltórios
    def separatingAxis(self):

        # Distância mínima, incialmente infinita
        min_dist = float('inf')

        # Iteramos para todos os pontos dos envoltórios
        for pt1 in self.ch1.hull:
            for pt2 in self.ch2.hull:
                # Caso a distância de um ponto seja menor que a distância atual
                # alteramos a distância para a distância atual 
                # e alteramos os pontos r e s para os pontos atuais
                actual_distance = dist(pt1,pt2)
                if(actual_distance < min_dist):
                    min_dist = actual_distance
                    self.r = pt1
                    self.s = pt2
        # Calculamos o ponto médio do segmento r, s. Os pontos de menor distância
        mid_point = Point((self.r.x+self.s.x)/2,(self.r.y+self.s.y)/2)

        # Pegamos os pontos da reta perpendicular à reta rs que passa pelo ponto médio
        self.p,self.q = mid_point, perpendicularLine(mid_point,self.r,self.s)

        # Verificamos qual classe está acima e qual está abaixo da reta
        if(ccw(self.p,self.q,self.r)):
            self.label1 = self.ch1.label
            self.label2 = self.ch2.label
        else:
            self.label1 = self.ch2.label
            self.label2 = self.ch1.label

    # Recebe um ponto e o classifica para a classe correspondente
    def classify(self,pt):

        # se não houver um classificador ger erro
        if(self.hasClassifier == False):
            raise Exception("Can't classify, classifier not implemented.")

        # aumentamos o número total de de pontos classificados
        self.total += 1

        # Rotúlo predito pelo classificador 
        pred_label = self.label1 if ccw(self.p,self.q,pt) else self.label2
        
        # Atualiza os TP,FP,TN e FN
        if(pred_label == self.label1):
            if(pt.label == self.label1):
                self.trueL1 += 1
            else:
                self.falseL1 += 1
        else:
            if(pt.label == self.label2):
                self.trueL2 += 1
            else:
                self.falseL2 += 1

        #Retorna o rótulo previsto
        return pred_label
    
    # Imprime as métricas conforme a formula
    def printMetrics(self):
        try:
            accuracy = (self.trueL1+self.trueL2)/self.total
            print('Accuracy: ',accuracy)
            precision = self.trueL1/(self.trueL1+self.falseL1)
            print('Precision: ',precision)
            recall = self.trueL1/(self.trueL1+self.falseL2)
            print('Recall', recall)
            fscore = 2*(precision*recall)/(precision+recall)
            print('F1: ',fscore)
        except:
            warnings.warn("Cannot calculate metrics due to a division by 0")

    
    



