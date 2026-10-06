from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

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

        heuristic = abs(root.state[0] - grid.end[0]) + abs(root.state[1] - grid.end[1]
        )

        frontier.add(root, priority=heuristic)

        while not frontier.is_empty():
            n = frontier.pop()

            for action in grid.actions(n.state):
                successor = grid.result(n.state, action)

                if successor in reached:
                    continue

                cost = n.cost + grid.individual_cost(n.state, action)

                son = Node(
                    "",
                    state=successor,
                    cost=cost,
                    parent=n,
                    action=action,
                )

                reached[successor] = cost

                if grid.objective_test(successor):
                    return Solution(son, reached)
                
                heuristic = abs(successor[0] - grid.end[0]) + abs(
                    successor[1] - grid.end[1]
                )

                frontier.add(son, priority=heuristic)

        return NoSolution(reached)
