from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...

        frontier= PriorityQueueFrontier() #creo frontera
        frontier.add(root)  #primer nodo, root

        while not frontier.is_empty(): #mientras haya nodos en frontera
            n = frontier.remove()
            if grid.objective_test(n.state):
                return Solution(n,reached) #si el nodo es el estado objetico, doy solucion

            for i in grid.actions(n.state):
                s= grid.result(n.state,i)
                if s not in reached:
                    nn = Node("", s, n.cost + grid.c(n.state, i), n, i)
                    reached[s]= nn.cost
                    frontier.add(nn)

        return NoSolution(reached)
