from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        frontier = PriorityQueueFrontier()
        frontier.add(root, priority=root.cost)

        while not frontier.is_empty():
            n = frontier.pop()

            if grid.objective_test(n.state):
                return Solution(n, reached)


            for action in grid.actions(n.state):
                successor = grid.result(n.state, action)
                cost = n.cost + grid.individual_cost(n.state, action)

                if successor in reached and reached[successor] <= cost:
                    continue

                son = Node(
                    "",
                    state=successor,
                    cost=cost,
                    parent=n,
                    action=action,
                )
                reached[successor] = cost
                
                frontier.add(son, priority=cost)


        return NoSolution(reached)
