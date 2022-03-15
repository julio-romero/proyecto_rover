import math
#from ast import Raise
#from inspect import Attribute
from unittest import result

from simpleai.search import SearchProblem
import simpleai.search as ss 
from random import randint as rd
from ambiente import crea_mapa_base
from simpleai.search.local import _exp_schedule
import os
import random


#Se usó como base el código "maze.py"


#Los estados son tuplas de coordenadas (x,y) que se verifican en el tablero
#En el _init_ se convierte a coordenadas el tablero
#En actions se usa el tablero para ver qué acción se puede tomar, pero el
#estado desde el principio es inicializado en la tupla y solamente se va actualizando

# Class containing the methods to solve the maze
class MazeSolver(SearchProblem):
    # Initialize the class
    def __init__(self, board):
        self.board = board #Recibe el tablero en formato lista de listas con strings
        super(MazeSolver, self).__init__(initial_state = self.generate_random_state())
        self.goal = (0, 0)

        #Busca en el tablero los puntos iniciales y finales    

    def generate_random_state(self):
        filas = len(self.board)
        cols = len(self.board[0])
        #print(cols)
        
        #print(equis, ye)
        while True:
            equis = rd(0,filas-1)
            ye = rd(0, cols-1)
            est = self.board[equis][ye]
            if est.isdigit():
                print("Posición aleatoria inicial (x, y):" ,equis,ye)
                print("Nivel inicial: ",est)
                print("")
                return(equis, ye)


    # Define the method that takes actions
    # to arrive at the solution   
    
    def actions(self, state):
        actions = []
        for action in COSTS.keys():
            x,y = state
            newy, newx = self.result(state, action)
            #print(newx,newy)
            if self.board[newy][newx] != '-' and self.board[newy][newx] != "#" and self.board[newy][newx] != "*":
                
                if abs(int(self.board[x][y]) - int(self.board[newy][newx]))<=1: #la diferencia de la nave no mayor a 1
                    actions.append(action)
                        
        return actions

    # Update the state based on the action
    def result(self, state, action):
        x, y = state
        #el if con que sea diferente de 0 es true
        #en los casos como "up","up right" y "up left" el count lo toma en 
        #cuenta y realiza el ajuste en la coordenada
        if action.count("up"):
            y -= 1
        if action.count("down"):
            y += 1
        if action.count("left"):
            x -= 1
        if action.count("right"):
            x += 1

        new_state = (x, y)

        return new_state

    # Check if we have reached the goal
    def value(self, state):
        x, y = state
        n = self.board[x][y]
        return int(n)


if __name__ == "__main__":
    # Define the map

    MAP = crea_mapa_base(5,8,2,5,mostrar_niveles = 1)
    #MAP = """
    ################################
    #43-43405532*1*005-3202035*2024#
    #1134-40203*0135211001051103145#
    #41442-11*244253342131555552403#
    #5511423234-0443-123--5-0230533#
    #13554024410435024014232-554354#
    #41044351435141-001-33*1341-435#
    #-04-4112-0043013-3451011052203#
    #40-305102421-3421N45443-00330-#
    #5-025513233-35*433-1513-001334#
    #2*202151002351455-3523001-*322#
    #--311302-0321001-410-130325532#
    #34043533232-0-230534023223-425#
    #404153-3525-310-31323333252050#
    #412-532-1130124012355554210324#
    #-053345-3552244304-50120425-12#
    ################################
    #"""
    # Convert map to a list
    print(MAP)
    MAP = [list(x) for x in MAP.split("\n") if x]

    # Define cost of moving around the map
    cost_regular = 1
    cost_diagonal = 1.4

    # Create the cost dictionary
    #No se incluye costo de moverse lateralmente
    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "up left": cost_diagonal,
        "up right": cost_diagonal,
        "down left": cost_diagonal,
        "down right": cost_diagonal,
    }

    # Create maze solver object
    print("_______________________________")
    problem = MazeSolver(MAP)
    print("_______________________________")
    print("- Algoritmo de Hill Climbing -")
    output = ss.hill_climbing(problem)
    print("Path:", output.path())
    sol= output.path()[0]
    coords= sol[1]
    y,x=coords
    print("Respuesta: ",MAP[y][x])
    print("_______________________________")
    print("- Algoritmo Random-Restart Hill Climbing -")
    output = ss.hill_climbing_random_restarts(problem,3)
    print("Path:", output.path())
    sol= output.path()[0]
    coords= sol[1]
    y,x=coords
    print("Respuesta: ",MAP[y][x])
    print("_______________________________")
    print("- Algoritmo de Simulated Annealing -")
    output = ss.simulated_annealing(problem,_exp_schedule)
    print("Path:", output.path())
    sol= output.path()[0]
    coords= sol[1]
    y,x=coords
    print("Respuesta: ",MAP[y][x])

 

