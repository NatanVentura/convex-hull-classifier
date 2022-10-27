# Utilities to use classifier

import matplotlib.pyplot as plt
from line_primitives import *
from point_primitives import *
from convex_hull import *
from classifier import *
import random


# Recebe os testes e o classificador
# Então imprime os resutlados
def plotTests(cl,test,l1):

    # Pega a coordenada dos pontos dos envoltórios
    ch = cl.ch1
    ch2 = cl.ch2
    coord = ch.hull
    coord2 =ch2.hull

    # Adiciona o primeiro ponto no envoltório, para "fechar o loop"
    coord2.append(coord2[0])
    coord.append(coord[0])

    # plota os envoltórios
    xs = list(map( lambda pt : pt.x, coord))
    ys = list(map( lambda pt : pt.y, coord))
    xs2 = list(map( lambda pt : pt.x, coord2))
    ys2 = list(map( lambda pt : pt.y, coord2))
    plt.figure()
    plt.plot(xs2,ys2)
    plt.plot(xs,ys) 

    # plota as coordenadas de todos os pontos do convex hull
    plt.scatter(list(map( lambda pt : pt.x, ch2.all_points)), list(map( lambda pt : pt.y, ch2.all_points)),alpha=0.5)
    plt.scatter(list(map( lambda pt : pt.x, ch.all_points)), list(map( lambda pt : pt.y, ch.all_points)),alpha=0.5)
    
    # caso tenha classificador, plota o eixo separador e os pontos de teste
    if(cl.hasClassifier):
        p,q = cl.p,cl.q
        qp = dist(q,p)
        lx = [p.x,q.x]
        ly = [p.y,q.y]
        plt.plot(lx,ly)
        plt.plot(lx,ly)
        plt.plot([cl.r.x,cl.s.x],[cl.r.y,cl.s.y],color='green')
    for pt in test:
        color = 'red' if(pt.label == l1) else 'purple'
        plt.scatter(pt.x,pt.y,color=color,alpha=0.3)
    
    # Mostra o gráfico na tela
    plt.show()

# Recebe um dataset, os rotúlos
# opcional: taxa de treino e seed
# Cria uma amostra e plota 
def sample(dataSet,l1,l2,trainTax=0.7,seed = 7):

    # Ordena os dados aleatóriamente e separa eles em treino e teste
    random.seed = seed
    random.shuffle(dataSet)
    trainSize = int(trainTax*len(dataSet))
    train,test = [],[]
    points1,points2 = [],[]
    train,test = dataSet[:trainSize],dataSet[trainSize:]

    # Associa cada ponto à seu respectivo rótulo
    for pt in train:
        if(pt.label == l1):
            points1.append(pt)
        elif(pt.label == l2):
            points2.append(pt)

    # Cria o classificador
    cl = Classifier(points1,points2,l1,l2)

    # Caso haja classificador classificamos os pontos de teste e imprimimos as métricas
    if cl.hasClassifier:
        for pt in test:
            cl.classify(pt)
        cl.printMetrics()

    # Os testes são plotados
    plotTests(cl,test,l1)

# Recebe dois inteiros, n e s
# Plota n testes aleatórios com s instâncias cada
def randomTests(n,s,seed = 7):
    random.seed = seed
    pts = []

    # Os testes são gerados num range no qual, 
    # geralmente, os dados estão linearmente separadas. 
    # Entretanto, eles podem não estar separados
    # assim podemos testar ambos os casos
    for i in range(n):
        pts = []
        A = random.randint(5,s-5)
        B = s - A
        for j in range(A):
            p = Point(random.randint(0,int(3*s)),random.randint(0,int(3*s)),"A")
            pts.append(p)
        for k in range(B):
            p = Point(random.randint(int(2.3*s),int(5*s)),random.randint(int(2.3*s),5*s),"B")
            pts.append(p)
        sample(pts,"A","B")
        
    
