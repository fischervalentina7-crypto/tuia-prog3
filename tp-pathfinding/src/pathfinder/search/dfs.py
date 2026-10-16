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
        frontier = StackFrontier()
        frontier.add(root)

        while not frontier.is_empty():
            n = frontier.remove()

            if n.state in expanded:
                continue

            expanded[n.state] = n

            if grid.objective_test(n.state):
                return Solution(n, expanded)

            for action in grid.actions(n.state):
                successor = grid.result(n.state, action)

                if successor not in expanded:
                    cost = n.cost + grid.c(n.state, action)

                    child = Node(
                        "",
                        state=successor,
                        cost=cost,
                        parent=n,
                        action=action,
                    )

                    frontier.add(child)

        return NoSolution(expanded)
