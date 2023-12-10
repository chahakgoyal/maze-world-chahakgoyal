from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:
    def __init__(self, maze):
        self.maze = maze
        self.start_state = []
        # all the locations that do not have a wall are valid possible locations for the blind robot
        for i in range(self.maze.width):
            for j in range(self.maze.height):
                if self.maze.is_floor(i, j):
                    self.start_state.append(i)
                    self.start_state.append(j)
        self.start_state = tuple(self.start_state)
        self.start_state = tuple(self.start_state)
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]
        # keeps track of the direction the robot is moving in
        self.moves_dict = {}
        self.moves_dict[(0, 1)] = "N"
        self.moves_dict[(1, 0)] = "E"
        self.moves_dict[(0, -1)] = "S"
        self.moves_dict[(-1, 0)] = "W"
        

    def __str__(self):
        string =  "Blind robot problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    # gets the successor state for every move that the robot is capable of performing
    def get_successors(self, state):
        # using a set to avoid duplicates
        successors = []
        # for every possible move
        for move in self.moves:
            succ = set()
            # get the new position after performing the move
            for i in range(0, len(state), 2):
                if self.legal_position((state[i] + move[0], state[i+1] + move[1])):
                    succ.add((state[i] + move[0], state[i+1] + move[1]))
                else:
                    # if it hits the wall, then the original state is still a possible state 
                    # because with that move, it will have to reverse
                    succ.add((state[i], state[i+1]))
            # create a tuple of all the states
            newsucc = []
            for i in succ:
                newsucc.append(i[0])
                newsucc.append(i[1])
            succ = tuple(newsucc)
            succ = tuple(succ)
            successors.append(succ)
        return tuple(successors)

    # transition cost is 0 if robot doesn't move or hits a wall and 1 otherwise
    def get_transition_cost(self, curr_state, prev_state):
        if curr_state == prev_state:
            return 0
        return 1

    # check if the position is valid - no walls
    def legal_position(self, position):
        if self.maze.is_floor(position[0], position[1]):
            return True
        return False

    # if there is only one possible location, the robot knows where 
    # it is and can hence follow a path from start to goal
    def goal_test(self, state):
        if len(state) == 2:
            return True
        return False
        
    # used in backchain method to convert states to directions that the robot can follow
    def word_path(self, curr_state, next_state):
        for move in self.moves:
            succ = set()
            for i in range(0, len(curr_state), 2):
                if self.legal_position((curr_state[i] + move[0], curr_state[i+1] + move[1])):
                    succ.add((curr_state[i] + move[0], curr_state[i + 1] + move[1]))
                else:
                    succ.add((curr_state[i], curr_state[i+1]))
            newsucc = []
            for i in succ:
                newsucc.append(i[0])
                newsucc.append(i[1])
            succ = tuple(newsucc)
            succ = tuple(succ)
            # return the move that when performed, yields the next state
            if succ == next_state:
                return self.moves_dict[move]


    # aids in changing the state path to direction path which is easier to read
    def backchain(self, state_path):
        words_path = []
        for i in range(len(state_path) - 1):
            words_path.append(self.word_path(state_path[i], state_path[i+1]))
        return words_path

    # here the heuristic is the number of possible locations of the robot
    # if the model has reached the goal - that is, the robot knows where it is,
    # then the heuristic will be 0
    def heuristic(self, state):
        heuristic = len(state)/2 - 1 
        return heuristic

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))


## A bit of test code
if __name__ == "__main__":
    test_maze3 = Maze("Downloads/provided/maze6.maz")
    test_problem = SensorlessProblem(test_maze3)
    print(test_maze3)
    print(test_problem.get_successors((0, 1, 1, 2, 4, 0, 2, 1, 7, 1, 0, 0, 3, 1, 6, 1, 4, 2, 8, 0, 0, 2, 5, 0, 1, 0, 8, 2, 5, 2)))
