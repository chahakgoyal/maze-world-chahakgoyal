from MazeworldProblem import MazeworldProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

# test_maze3 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze3.maz")
# test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

# # print(test_mp.get_successors(test_mp.start_state))

# # this should explore a lot of nodes; it's just uniform-cost search
# # result = astar_search(test_mp, null_heuristic)
# # print(result)
# # test_mp.animate_path(result.path)

# # # # this should do a bit better:
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# # Your additional tests here:
# test_maze8 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze8.maz")
# test_mp = MazeworldProblem(test_maze8, (1, 4, 1, 3, 1, 2))

# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)


# test_maze2 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze2.maz")
# # print(test_maze2)
# test_mp = MazeworldProblem(test_maze2, (1, 3))

# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# test_mp1 = MazeworldProblem(test_maze2, (2, 1))
# result = astar_search(test_mp1, test_mp1.manhattan_heuristic)
# print(result)
# test_mp1.animate_path(result.path)

# test_maze9 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze9.maz")
# test_mp = MazeworldProblem(test_maze9, (3, 1, 1, 3, 5, 3))

# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# test_maze10 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze10.maz")
# test_mp = MazeworldProblem(test_maze10, (3, 3, 4, 3))

# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)

test_maze11 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze11.maz")
test_mp = MazeworldProblem(test_maze11, (4, 3, 4, 4))

result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze12 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze12.maz")
test_mp = MazeworldProblem(test_maze12, (12, 3, 13, 2))

result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)