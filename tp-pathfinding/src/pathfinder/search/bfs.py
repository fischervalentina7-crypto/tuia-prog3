from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...
        if (grid.objective_test(root.state)):
            return Solution(root)
        
        frontier = QueueFrontier()
        frontier.add(root)

        while not frontier.is_empty():
            n = frontier.remove()
            for i in grid.actions(n.state):
                s= grid.result(n.state, i)
                if s not in reached:
                    nn = Node("", s, n.cost + grid.c(n.state, i), n, i)

                    reached[s] = True

                    if grid.objective_test(s):
                        return Solution(nn, reached)

                    frontier.add(nn)


        return NoSolution(reached)
