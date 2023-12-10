from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]   # all the directions that robot can move in if
        # the robot doesn't stay in the same place it is its turn to move
        self.maze = maze
        # first robot is supposed to move first hence appending 0 
        # to the start_state where 0 corresponds to the first robot
        self.start_state = [0]
        self.robotnumber = len(self.maze.robotloc)/2   # number of robots in the maze
        for i in range(len(self.maze.robotloc)):
            self.start_state.append(self.maze.robotloc[i])    # add locations of the robots to the start state
        self.start_state = tuple(self.start_state)
        self.goal_locations = []    # get the goal locations
        for i in range(len(goal_locations)):
            self.goal_locations.append(goal_locations[i])
        self.goal_locations = tuple(self.goal_locations)   # used tuple data structure since it is one of the best data structures to use in this case

    def __str__(self):
        string =  "Mazeworld problem: "
        return string

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    # return the manhattan distance from the current state of robots to their goal states
    def manhattan_heuristic(self, state):
        heuristic = 0
        state = state[1:]
        for i in range(len(state)):
            heuristic += abs(state[i] - self.goal_locations[i])
        return heuristic

    # check if the current location is legal or not
    def legalBlocks(self, block, locations):  
        x = False
        # check if the new location is not a wall or an obstacle
        if self.maze.is_floor(block[0], block[1]):
            for i in locations:
                # check if there is another robot in the spot
                if block[0] != i[0] or block[1] != i[1]:
                    x = True
                else:
                    return False
        return x

    # if robot doesn't move then the transition cost is 0 else it is 1    
    def get_transition_cost(self, curr_state, prev_state):
        if curr_state[1:] == prev_state[1:]:
            return 0
        return 1

    # appends valid next locations to successors of current state
    def append_fn(self, locations, successors):
        succ = [(int) ((self.which_robot + 1) % self.robotnumber)]
        for i in locations:
            succ.append(i[0])
            succ.append(i[1])
        successors.append(tuple(succ))


    # get successors of the current state by moving the robot which is to move now
    def get_successors(self, state):
        # which robot's turn is it to move?
        self.which_robot = state[0]  
        locations = []
        for i in range(1, len(state) - 1, 2):
            locations.append([state[i], state[i + 1]])  # get the current location of the robots
        successors = []
        x = locations[self.which_robot][0]  # for each robot, get its x and y coordinates 
        y = locations[self.which_robot][1]

        # for every possible way in which the robot can move
        for move in self.moves:
            # check if the new location found after moving the robot in a certain direction is valid
            if self.legalBlocks((x + move[0], y + move[1]), locations):
                # update locations to add it to successors
                locations[self.which_robot][0] = x + move[0]
                locations[self.which_robot][1] = y + move[1]
                self.append_fn(locations, successors)
                locations[self.which_robot][0] = x
                locations[self.which_robot][1] = y
            # append the current location
            self.append_fn(locations, successors)
        return successors

    
    # check if the current state is the goal state
    def goal_test(self, state):
        x = False
        state = state[1:]
        for i in range(len(state)):
            if state[i] == self.goal_locations[i]:
                x = True
            else:
                return False
        return x


    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("/Users/chahak/Downloads/provided/maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
    print(test_mp.get_successors((0, 1, 4, 2, 2, 3, 1)))
