""" Codigo del libro con modificaciones y comentarios mios"""

from ast import Raise
from inspect import Attribute
import math
from ambiente import crea_mapa_base
from simpleai.search import SearchProblem, astar, greedy, uniform_cost

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
                    self.board[y][x] = 3 #asignamos al lugar incial de la nave el numero 1
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
                if abs(int(self.board[y][x]) - int(self.board[newy][newx]))<=1: #la diferencia de la nave no mayor a 1
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
    MAP = crea_mapa_base(15,30,20,50,mostrar_niveles = 1)

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
    try:
        problem = MazeSolver(MAP)
    except AttributeError:
        print("Error en la generacion del mapa aleatorio, usando mapa por defecto")
        print("Agua  20 Obs  98 Nave en 10,22")
        MAP = """
        ################################
        #      -* -         ---     -- #
        #     -     -     *   - *- - --#
        # -  -           -  *      - - #
        #     -   * -         -  ----  #
        # -    -   *  -    -  - - -  - #
        #       - -   - -*-- -         #
        #        *  -*-    --      -   #
        # *  *--- -  *-- -          -  #
        #            *   *- *  **      #
        #      * ----    *  --N-- -    #
        #      -  - -       --    ---  #
        # ----    -   -   -  -       - #
        #         --       - -        -#
        # * --     -       --          #
        #   -   - -     --    -  -     #
        ################################
        """
        problem = MazeSolver(MAP)


    # Run the solver
    result = astar(problem, graph_search=True)
    #result = greedy(problem,True) #sin el True, tarda muchísimo
    #result = uniform_cost(problem,True) #sin el True, tarda muchísimo
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
                    print('o', end='')
                else:
                    print(MAP[y][x], end='')

            print()
    except AttributeError or NameError:
        raise AttributeError ("Algo salio mal, corre de nuevo la funcion")

