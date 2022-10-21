from decimal import DecimalTuple
import numpy as np 
import sys
import math

def RegistroCiudad(hormiga,ciudad,ciudadesVisitadas):
   ciudadesVisitadas[hormiga][ciudad] = 1
   return ciudadesVisitadas



def visitaInicial(hormigas_size,numVariables):
   trayectoriahormiga = np.full((hormigas_size,numVariables),1)
   ciudadesVisitadas = np.full((hormigas_size,numVariables),0)
   for i in range(0,hormigas_size):
      ciudad = np.random.randint(numVariables,dtype=int)
      trayectoriahormiga[i][0] = ciudad
      ciudadesVisitadas = RegistroCiudad(i,ciudad,ciudadesVisitadas)
      
   print(trayectoriahormiga,ciudadesVisitadas)

   return trayectoriahormiga,ciudadesVisitadas




# py .\main.py berlin52.txt 10 10 100 0.1 2.5 0.9

if len(sys.argv) == 8 :
   archivo_entrada = sys.argv[1]
   seed = int(sys.argv[2])
   hormigas_size = int(sys.argv[3])
   iteraciones = int(sys.argv[4])
   factor_feromona = float(sys.argv[5])
   peso_heuristica = float(sys.argv[6])
   prob_limite = float(sys.argv[7])
else:
   print('Formato de argumentos ingresados no es válido: <Nombre archivo de entrada> <Valor semilla> <Cantidad hormigas> <Iteraciones> <Factor evaporacion feromona> <Peso heuristica> <Probabilidad del limite>.')
   exit()

def solucionCalculaCosto(n,s,c):
   aux = c[s[n-1]][s[0]]
   for i in range(n-1):
      aux += c[s[i]][s[i+1]]
   return aux

#inicializamos el seed
np.random.seed(seed=seed)
#Leemos el archivo 
coordenadas = np.genfromtxt(archivo_entrada,delimiter=" ",skip_footer=1,skip_header=6,dtype=int)
numVariables = coordenadas.shape[0]
print(coordenadas)

trayectoriahormiga,ciudadesVisitadas = visitaInicial(hormigas_size,numVariables)

""" print(ciudadvisitada)

Distancia = np.full((coordenadas.shape[0],coordenadas.shape[0]),-1,dtype=float)
#print(Distancia)
for i in range(0,len(Distancia)):
   for j in range(i+1,len(Distancia)):
      distancia = math.sqrt(math.pow(coordenadas[i][1]-coordenadas[j][1],2)+math.pow(coordenadas[i][2]-coordenadas[j][2],2))
      Distancia[i][j] = distancia
      Distancia[j][i] = distancia

Heuristica = np.full_like(Distancia,fill_value=1/Distancia,dtype=float)
solucionMejor = np.arange(0,coordenadas.shape[0])
np.random.shuffle(solucionMejor)
solucionMejorCosto = solucionCalculaCosto(numVariables,solucionMejor,Distancia) """
#Tij0 = 1/(numVariables*solucionMejorCosto)
#matrizFeromona = np.full_like(Distancia,fill_value=Tij0,dtype=float)
#print(matrizFeromona)
#print(solucionMejorCosto)





