from simpleai.search import SearchProblem, astar
import sqlite3
 
GOAL = 'FU22s22CK'
 
class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            return list(' 312648712648716578137658148129479821612983ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []
 
    def result(self, state, action):
        return state + action
 
    def is_goal(self, state):
        return state == GOAL
 
    def heuristic(self, state):
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing
 
 
problem = HelloProblem(initial_state='')
result = astar(problem)
 
print result.state
print result.path()