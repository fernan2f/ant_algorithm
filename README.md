# # Algoritmo colonia de Hormigas para el problema del Vendedor viajero 

En este algoritmo se resolverá el problema del vendedor viajero, el cual consiste buscar la ruta mas optimo que pase por 52 ciudades de Berlín. Esto se realizara mediante el lenguaje de programacion python


## Instalación

1. Asegurate de tener instalado <a href="https://www.python.org/">Python</a> >= `3.0`

2. Instalar libreria numpy 
   ```sh
   pip install numpy
   ```
 
 ## Ejecución
 
   1. Para iniciar el algoritmo de debe ejecutar por consola el siguiente comando
   ```sh
   python3 main.py  <Nombre archivo de entrada> <Valor de la semilla> <Cantidad hormigas> <Iteraciones> <Factor evaporacion feromona> <Peso heuristica> <Probabilidad del limite>
   ```
Los parámetros de entradas serán de tipo:
* Nombre archivo de entrada: Variable de tipo `string` con el nombre del archivo .txt que contenga las distancia de las ciudades
* Valor de la semilla: Generador de los valores aleatorios. (Para una misma semilla se obtendrá siempre los mismos valores aleatorios) Es de cualquier tipo de variable
* Cantidad hormigas : Numero de hormigas que realizan la búsqueda de su objetivo de tipo `entero`
* Iteraciones :  Variable de tipo `entero` del número de siglos que se representa cuando la hormiga logran su objetivo
* Factor evaporación feromona : Variable que nos da el factor de evaporación de la feromona, es de tipo `decimal` entre 0 y 1
* Peso heurística : Es el peso del valor de la heurística.
* Probabilidad del límite : Es un valor de probabilidad límite predefinido mayor o igual que 0 y menor o igual que 1.

 


## Parámetros de salida

* Archivo dato.txt con la mejor trayectoria encontrada.

## Desarrolladores

* Fernando Fuentealba
* Bernardo Fernández
* Alexis Pinto
