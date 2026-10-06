from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...
        if (grid.objective_test(root)):
            return Solution(root)

        frontier = StackFrontier()
        frontier.add(root)

        while not frontier.is_empty(): 
            n = frontier.remove()

            for i in grid.actions(n.state):
                s = grid.result(n.state, i)
                nn = Node("", s, n.cost + grid.c(n.state, i), n, i)


            
        return NoSolution(expanded)
