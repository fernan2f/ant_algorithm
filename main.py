import numpy as np 
import sys
import math


def RegistroCiudad(hormiga,ciudad,ciudadesVisitadas):
   ciudadesVisitadas[hormiga][ciudad] = 0
   return ciudadesVisitadas

def random_int_to_n(n):
   return np.random.randint(n)

def random_0_to_1():
   return np.random.random()

def visitaInicial(hormigas_size,numVariables):
   trayectoriahormiga = np.full((hormigas_size,numVariables),1)
   ciudadesVisitadas = np.full((hormigas_size,numVariables),1)
   for i in range(0,hormigas_size):
      ciudad = random_int_to_n(numVariables)
      trayectoriahormiga[i][0] = ciudad
      ciudadesVisitadas = RegistroCiudad(i,ciudad,ciudadesVisitadas)
   return trayectoriahormiga,ciudadesVisitadas

#Calcula la probabilidad que tiene un individuo en el torneo
def arrayTorneo(arrayFitness,numCiudades):
    arrayTorneo = np.empty(numCiudades)
    acc = 0
    for i in range(0,numCiudades):
        acc = acc + arrayFitness[i]
        arrayTorneo[i] = acc
    return arrayTorneo


#Se obtiene el indice de un individuo de la poblacion randomicamente segun la probabilidad de cruza
def getIndexTorneo(random, arrayProbCruza):
    for i in range(0, numCiudades):
        if random <= arrayProbCruza[i]:
            return i


#def TxN(heuristica,Feromona,CiudadesVisitadas):




# py .\main.py berlin52.txt 10 10 100 0.1 2.5 0.9

# if len(sys.argv) == 8 :
#    archivo_entrada = sys.argv[1]
#    seed = int(sys.argv[2])
#    hormigas_size = int(sys.argv[3])
#    iteraciones = int(sys.argv[4])
#    factor_feromona = float(sys.argv[5])
#    peso_heuristica = float(sys.argv[6])
#    prob_limite = float(sys.argv[7]) #q_0
# else:
#    print('Formato de argumentos ingresados no es válido: <Nombre archivo de entrada> <Valor semilla> <Cantidad hormigas> <Iteraciones> <Factor evaporacion feromona> <Peso heuristica> <Probabilidad del limite>.')
#    exit()

archivo_entrada = 'berlin.txt'
seed = 10
hormigas_size = 10
iteraciones = 100
factor_feromona = 0.1
peso_heuristica =  2.5
prob_limite = 0.9 #q_0

def solucionCalculaCosto(n,s,c):
   aux = c[s[n-1]][s[0]]
   for i in range(n-1):
      aux += c[s[i]][s[i+1]]
   return aux

#inicializamos el seed
np.random.seed(seed=seed)
#Leemos el archivo 
coordenadas = np.genfromtxt(archivo_entrada,delimiter=" ",skip_footer=1,skip_header=6,dtype=int)
numCiudades = coordenadas.shape[0]




Distancia = np.full((coordenadas.shape[0],coordenadas.shape[0]),-1,dtype=float)

#print(Distancia)
for i in range(0,len(Distancia)):
   for j in range(i+1,len(Distancia)):
      distancia = math.sqrt(math.pow(coordenadas[i][1]-coordenadas[j][1],2)+math.pow(coordenadas[i][2]-coordenadas[j][2],2))
      Distancia[i][j] = distancia
      Distancia[j][i] = distancia 

Heuristica = np.full_like(Distancia,fill_value=1/Distancia,dtype=float)
np.fill_diagonal(Heuristica,0) # OTRA SOLUCION SERÍA RELLENAR LA DIAGONAL CON 1 O -1??
solucionMejor = np.arange(0,coordenadas.shape[0])
np.random.shuffle(solucionMejor)
print(solucionMejor)
solucionMejorCosto = solucionCalculaCosto(numCiudades,solucionMejor,Distancia)
Tij0 = 1/(numCiudades*solucionMejorCosto)
matrizFeromona = np.full_like(Distancia,fill_value=Tij0,dtype=float)



num_iteraciones = 0
index_mejor_solucion = -1

while num_iteraciones < iteraciones or solucionMejorCosto == 7544.3659:
   trayectoriahormiga,ciudadesVisitadas = visitaInicial(hormigas_size,numCiudades)
   
   #print(ciudadesVisitadas)
   for i in range(0,numCiudades-1 ):
      for j in range(0,hormigas_size):
         prob_ecuacion_1 = random_0_to_1()
         TxN = ciudadesVisitadas[j] * matrizFeromona[j] * Heuristica[j]**peso_heuristica
         indexVisitado = 0   
         if (prob_ecuacion_1 < prob_limite):
            indexVisitado = np.random.choice(np.where(TxN == np.amax(TxN))[0])
            ciudadesVisitadas[j][indexVisitado] = 0
            trayectoriahormiga[j][i+1] = indexVisitado
         else:
            ciudadesRestantes = ciudadesVisitadas[j]
            if(ciudadesRestantes[np.where(ciudadesRestantes == 1)].size > 0 and np.sum(TxN) > 0):
               j0 = (TxN)/np.sum(TxN)
               arrayTorneos = arrayTorneo(j0,numCiudades)
               random = random_0_to_1()
               indexVisitado = getIndexTorneo(random, arrayTorneos)
               trayectoriahormiga[j][i+1] = indexVisitado
               ciudadesVisitadas[j][indexVisitado] = 0   
            elif(ciudadesRestantes[np.where(ciudadesRestantes == 1)].size > 0):
               indexVisitado = np.where(ciudadesRestantes==1)[0][0]
               trayectoriahormiga[j][i+1] = indexVisitado
               ciudadesVisitadas[j][indexVisitado] = 0   
               
         matrizFeromona[j][indexVisitado] = (1-factor_feromona)*matrizFeromona[j][indexVisitado] + factor_feromona * Tij0
         matrizFeromona[indexVisitado][j] = matrizFeromona[j][indexVisitado]
      matrizFeromona[j][-1] = (1-factor_feromona)*matrizFeromona[j][indexVisitado] + factor_feromona * Tij0
      matrizFeromona[j][0] = (1-factor_feromona)*matrizFeromona[j][indexVisitado] + factor_feromona * Tij0  
      
   
   for k in range(0,len(trayectoriahormiga)):
      aux = solucionCalculaCosto(numCiudades,trayectoriahormiga[k],Distancia)
      if(aux < solucionMejorCosto):
         solucionMejorCosto = aux
         Tij0 = 1/(numCiudades*solucionMejorCosto)
         index_mejor_solucion = k
         solucionMejor = trayectoriahormiga[k]  
  
   for l in (solucionMejor):
      matrizFeromona[index_mejor_solucion][l] = (1-factor_feromona)*matrizFeromona[index_mejor_solucion][l] + factor_feromona * (1/solucionMejorCosto)

   num_iteraciones += 1
   print("mejor ", solucionMejorCosto , " i ", num_iteraciones)
   

   


#  print(ciudadvisitada)
# print(trayectoriahormiga)



print(matrizFeromona[45])


