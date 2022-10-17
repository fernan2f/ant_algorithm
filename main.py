import numpy as np 
import sys

# py .\main.py berlin52.txt 10 10 100 0.1 2.5 0.9

if len(sys.argv) == 8 :
   archivo_entrada = sys.argv[1]
   seed = sys.argv[2]
   hormigas_size = int(sys.argv[3])
   iteraciones = int(sys.argv[4])
   factor_feromona = float(sys.argv[5])
   peso_heuristica = float(sys.argv[6])
   prob_limite = float(sys.argv[7])
else:
   print('Formato de argumentos ingresados no es válido: <Nombre archivo de entrada> <Valor semilla> <Cantidad hormigas> <Iteraciones> <Factor evaporacion feromona> <Peso heuristica> <Probabilidad del limite>.')
   exit()

coordenadas = np.genfromtxt(archivo_entrada,delimiter=" ",skip_footer=1,skip_header=6,dtype=int)

Distancia = np.zeros((coordenadas.shape[0],coordenadas.shape[0]))
Heuristica = np.copy(Distancia)

print(list(coordenadas.shape))

