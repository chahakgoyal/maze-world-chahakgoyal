from re import search
from SearchSolution import SearchSolution
from heapq import heapify, heappop, heappush, heappushpop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        # you write this part
        return self.heuristic + self.transition_cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()



# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


# astar search that finds the optimal solution
def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_state = search_problem.start_state
    start_node = AstarNode(start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)
    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)
    visited_cost = {}
    visited_cost[start_node.state] = 0
    # you write the rest:
    # while there are still elements in the priority queue
    while pqueue:
        # get the element that has the minimum total cost
        node = heappop(pqueue)
        # the number of nodes visited has increased
        solution.nodes_visited += 1
        # if goal state has been found then backchain and return path
        if search_problem.goal_test(node.state):  
            solution.path = backchain(node)
            solution.cost = node.transition_cost
            return solution
        # otherwise get successors
        successors = search_problem.get_successors(node.state)
        # for every state in successors
        for child in successors:
            # returns 0 if the robot doesn't move and 1 otherwise
            transition_cost = search_problem.get_transition_cost(child, node.state)
            childnode = AstarNode(child, heuristic_fn(child), node, node.transition_cost + transition_cost)
            # if child has not been explored, add it to priority queue
            if childnode.state not in visited_cost:
                visited_cost[childnode.state] = childnode.transition_cost
                heappush(pqueue, childnode)
            # if child has been explored but this time around
            # the child has lower cost, update the priority queue with new cost of the child
            elif childnode.state in visited_cost:
                if visited_cost[childnode.state] > childnode.transition_cost:
                    visited_cost[childnode.state] = childnode.transition_cost
                    heappush(pqueue, childnode)
    return solution