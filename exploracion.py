""" Codigo del libro con modificaciones y comentarios mios"""

import math
from ast import Raise
from inspect import Attribute
from unittest import result

from simpleai.search import SearchProblem, astar, greedy, uniform_cost
from random import randint as rd
from ambiente import crea_mapa_base

#Los estados son tuplas de coordenadas (x,y) que se verifican en el tablero
#En el _init_ se convierte a coordenadas el tablero
#En actions se usa el tablero para ver qué acción se puede tomar, pero el
#estado desde el principio es inicializado en la tupla y solamente se va actualizando

# Class containing the methods to solve the maze
class MazeSolver(SearchProblem):
    # Initialize the class 
    def __init__(self, board):
        self.board = board #Recibe el tablero en formato lista de listas con strings
        self.goal = (0, 0)

        #Busca en el tablero los puntos iniciales y finales
        #Toma en cuenta que en la orilla izquierda del tablero hay 4 espacios
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == "N":
                    self.initial = (x, y)
                    self.board[y][x] =  rd(0,5)
                elif self.board[y][x] == "*":
                    self.goal = (x, y)
        
        super(MazeSolver, self).__init__(initial_state=self.initial)


    # Define the method that takes actions
    # to arrive at the solution
    def actions(self, state):
        actions = []
        for action in COSTS.keys():
            x,y = self.result(state,action)
            newx, newy = self.result(state, action)
            if self.board[newy][newx] != '-' and self.board[newy][newx] != "#":
                try: 
                    if self.board[newy][newx] != '*':
                        pass
                    if abs(int(self.board[y][x]) - int(self.board[newy][newx]))<=1: #la diferencia de la nave no mayor a 1
                        actions.append(action)
                    else:
                        pass
                except ValueError:
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
    def is_goal(self, state):
        return state == self.goal

    # Compute the cost of taking an action
    def cost(self, state, action, state2):
        return COSTS[action]

    # Heuristic that we use to arrive at the solution
    def heuristic(self, state):
        x, y = state
        gx, gy = self.goal

        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)

if __name__ == "__main__":
    # Define the map

    #MAP = crea_mapa_base(20,150,200,500,mostrar_niveles = 1,locacion_nave=[1,2])
    MAP = """
    ################################
    #43-43405532*1*005-3202035*2024#
    #1134-40203*0135211001051103145#
    #41442-11*244253342131555552403#
    #5511423234-0443-103--5-0230533#
    #13554024410435024014232-554354#
    #41044351435141-001-33*1341-435#
    #-04-4112-0043013-3451011052203#
    #40-305102421-3421045443-00330-#
    #5-025513233-35*433-1513-001334#
    #2*202151002351455-3523001-*322#
    #--311302-0321001-410-130325532#
    #34053533232-0-230534023223-425#
    #404153-3525-N10-31323333252050#
    #412-532-1130124012355554210324#
    #-053345-3552244304-50120425-12#
    ################################
    """
    # Convert map to a list
    print(MAP)
    MAP = [list(x) for x in MAP.split("\n") if x]

    # Define cost of moving around the map
    cost_regular = 1
    cost_diagonal = 1

    # Create the cost dictionary
    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "left": cost_regular,
        "right": cost_regular,
        "up left": cost_diagonal,
        "up right": cost_diagonal,
        "down left": cost_diagonal,
        "down right": cost_diagonal,
    }

    # Create maze solver object
    problem = MazeSolver(MAP)


    # Run the solver
    #result = greedy(problem, graph_search=True)
    #result = uniform_cost(problem,True) #sin el True, tarda muchísimo
    result = astar(problem,graph_search=True)
    try:
        path = [x[1] for x in result.path()]


        # Print the result
        print()
        for y in range(len(MAP)):
            for x in range(len(MAP[y])):
                if (x, y) == problem.initial:
                    print('N', end='')
                elif (x, y) == problem.goal:
                    print('N', end='')
                elif (x, y) in path:
                    print('>', end='')
                else:
                    print(MAP[y][x], end='')

            print()
    except AttributeError or NameError:
        raise AttributeError ("Algo salio mal, corre de nuevo la funcion")

