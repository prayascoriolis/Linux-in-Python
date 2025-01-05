"""29. Implement the A* search algorithm for pathfinding in a grid."""

import heapq


class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid(self, x, y):
        # Check if a cell is valid (within bounds and not an obstacle).
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0

    def heuristic(self, x1, y1, x2, y2):
        # Heuristic function: Manhattan distance.
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star(self, start, goal):
        """
            start: (start_x, start_y): the starting position.
            goal: (goal_x, goal_y): the goal position.
        Returns: List of tuples representing the path
        """
        # Priority queue for the open set
        open_set = []
        heapq.heappush(open_set, (0, start))  # (f_score, node)
        # Dictionaries to store g-scores and the path
        g_score = {start: 0}
        came_from = {}
        # Directions for moving in 4 directions (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while open_set:
            # Get the node with the lowest f_score
            _, current = heapq.heappop(open_set)
            # If we reach the goal, reconstruct the path
            if current == goal:
                return self.reconstruct_path(came_from, current)
            x, y = current
            # Explore neighbors
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if not self.is_valid(neighbor[0], neighbor[1]):
                    continue
                # Calculate tentative g-score for the neighbor
                tentative_g_score = g_score[current] + 1  # Assuming uniform cost
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # Update the g-score and f-score
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(
                        neighbor[0], neighbor[1], goal[0], goal[1]
                    )
                    heapq.heappush(open_set, (f_score, neighbor))
                    # Update the path
                    came_from[neighbor] = current
        # If no path is found
        return []

    def reconstruct_path(self, came_from, current):
        # Reconstruct the path from start to goal.
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(current)
        return path[::-1]


if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]

    astar = AStar(grid)
    start = (0, 0)
    goal = (4, 4)
    path = astar.a_star(start, goal)
    print("Path:", path)
