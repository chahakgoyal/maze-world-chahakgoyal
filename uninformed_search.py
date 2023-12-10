
from collections import deque
from re import S, search
from SearchSolution import SearchSolution

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        # you write this part
        self.state = state
        self.parent = parent

# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions

def bfs_search(search_problem):
    solution = SearchSolution(search_problem, "BFS")
    # queue keeps track of what node to visit next
    nqueue = deque()
    start_state = search_problem.start_state
    node = SearchNode(start_state)
    nqueue.append(node)
    # set keeps track of what nodes have already been visited
    explored = set()
    # pred stack keeps track of the path so far
    pred = []
    while len(nqueue) > 0:
        node = nqueue.popleft()
        if node not in explored:
            state = node.state
            explored.add(node.state)
            # backtracking if goal state is found
            if search_problem.goal_test(state):
                pred.append(state)
                while node.parent is not None:
                    pred.append(node.parent.state)
                    node = node.parent
                # save the path in solution
                while pred:
                    solution.path.append(pred.pop())
                solution.nodes_visited = len(explored)
                return solution
            # if current state is not goal state
            for i in search_problem.get_successors(state):
                if i not in explored:
                    childnode = SearchNode(i, node)
                    nqueue.append(childnode)
    solution.nodes_visited = len(explored)
    return solution
    
            
    

# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search(search_problem, depth_limit=100, solution=None, node=None, path=None):
    # if no node object given, create a new search from starting state
    # keeps track of the path so far
    if path is None:
        path = []
    
    if node == None:
        solution = SearchSolution(search_problem,"DFS")
        node = SearchNode(search_problem.start_state)
        solution.nodes_visited = 1
    path.append(node.state)
    
    # check if the depth_limit has been reached or not
    if depth_limit >= 0:
        
        # base case --> goal state is found
        if search_problem.goal_test(node.state):
            solution.path = path
            return solution
        else:
            # if there are successors
            if search_problem.get_successors(node.state):
                for i in search_problem.get_successors(node.state): 
                    solution.nodes_visited += 1
                    # if the node has not been explored yet
                    if i not in path:
                        newnode = SearchNode(i, node)
                        # recursive call
                        successor_solution = dfs_search(search_problem, solution=solution, depth_limit=depth_limit - 1, node=newnode, path=path)
                        # if solution has been found, return it
                        if successor_solution:
                            if search_problem.goal_state in successor_solution.path:
                                return successor_solution
            # if the node that was in the path has no successors or all its successors have been visited in the past, remove that node as it is not a part of the final path            
            path.pop()
        return solution
    else:
        return solution

def ids_search(search_problem, depth_limit=100):
    # you write this part
    
    # loop around dfs until either graph limit has been reached or depth_limit has been reached
    solution = SearchSolution(search_problem, "IDS")
    i = 0
    while i <= depth_limit:
        solution.nodes_visited += dfs_search(search_problem, depth_limit=i).nodes_visited
        if dfs_search(search_problem, depth_limit=i).path:
            solution.path = dfs_search(search_problem, depth_limit=i).path
            break
        elif len(dfs_search(search_problem, depth_limit=depth_limit).path) == 0:
            if dfs_search(search_problem, depth_limit=depth_limit).nodes_visited > dfs_search(search_problem, depth_limit=i).nodes_visited:
                solution.nodes_visited += dfs_search(search_problem, depth_limit=i).nodes_visited
            else:
                solution.nodes_visited += dfs_search(search_problem, depth_limit=i).nodes_visited
                break

        i += 1
    return solution