# You write this:
from SensorlessProblem import SensorlessProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

test_maze6 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze6.maz")
test_mp = SensorlessProblem(test_maze6)

# print(test_mp.get_successors(test_mp.start_state))
def null_heuristic(state):
    return 0
# this should explore a lot of nodes; it's just uniform-cost search
# result = astar_search(test_mp, null_heuristic)
# test_mp.animate_path(result.path)
# result.path = test_mp.backchain(result.path)
# print(result)

# result = astar_search(test_mp, test_mp.heuristic)
# test_mp.animate_path(result.path)
# result.path = test_mp.backchain(result.path)
# print(result)


# test_maze7 = Maze("Downloads/provided/maze7.maz")
# test_mp = SensorlessProblem(test_maze7)
# result = astar_search(test_mp, test_mp.heuristic)
# test_mp.animate_path(result.path)
# result.path = test_mp.backchain(result.path)
# print(result)



# test_maze1 = Maze("Downloads/provided/maze1.maz")
# test_mp = SensorlessProblem(test_maze1)
# result = astar_search(test_mp, test_mp.heuristic)
# test_mp.animate_path(result.path)
# result.path = test_mp.backchain(result.path)
# print(result)

# test_maze4 = Maze("Downloads/provided/maze4.maz")
# test_mp = SensorlessProblem(test_maze4)
# result = astar_search(test_mp, test_mp.heuristic)
# test_mp.animate_path(result.path)
# result.path = test_mp.backchain(result.path)
# print(result)

# test_maze13 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze13.maz")
# test_mp = SensorlessProblem(test_maze13)
# result = astar_search(test_mp, test_mp.heuristic)
# test_mp.animate_path(result.path)
# result.path = test_mp.backchain(result.path)
# print(result)

test_maze14 = Maze("Desktop/dartmouth/22f/cs76/maze_world/maze14.maz")
test_mp = SensorlessProblem(test_maze14)
result = astar_search(test_mp, test_mp.heuristic)
test_mp.animate_path(result.path)
result.path = test_mp.backchain(result.path)
print(result)