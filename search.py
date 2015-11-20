# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from game import Directions
    from util import Stack
    South = Directions.SOUTH
    West = Directions.WEST
    East = Directions.EAST
    North = Directions.NORTH
    stop = Directions.STOP

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    ans = []
    ParentNode = {}
    direction = {}
    stack = Stack()
    startNode = problem.getStartState()
    visitedList = []
    stack.push(startNode)
    if problem.isGoalState(startNode):
        return stop

    while stack.isEmpty() == False:
        currentNode = stack.pop()
        visitedList.append(currentNode)
        if problem.isGoalState(currentNode):
            goalPath = currentNode
            while goalPath != startNode:
                ans.append(direction[goalPath])
                goalPath = ParentNode[goalPath]
            return ans[::-1]
        allCurrentSuccessor = problem.getSuccessors(currentNode)
        for Node in allCurrentSuccessor:
            if not Node[0] in visitedList:
                stack.push(Node[0])
                ParentNode[Node[0]] = currentNode
                direction[Node[0]] = Node[1]

    print "can't find goal"
    return stop
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Queue
    South = Directions.SOUTH
    West = Directions.WEST
    East = Directions.EAST
    North = Directions.NORTH
    stop = Directions.STOP

    ans = []
    ParentNode = {}
    direction = {}
    queue = Queue()
    startNode = problem.getStartState()
    visitedList = []
    queue.push(startNode)
    if problem.isGoalState(startNode):
        return stop

    while queue.isEmpty() == False:
        currentNode = queue.pop()
        if not currentNode in visitedList:
            visitedList.append(currentNode)
        if problem.isGoalState(currentNode):
            goalPath = currentNode
            while goalPath != startNode:
                ans.append(direction[goalPath])
                goalPath = ParentNode[goalPath]
            return ans[::-1]
        allCurrentSuccessor = problem.getSuccessors(currentNode)
        for Node in allCurrentSuccessor:
            if not Node[0] in visitedList:
                queue.push(Node[0])
                visitedList.append(Node[0])
                ParentNode[Node[0]] = currentNode
                direction[Node[0]] = Node[1]
                print Node[0],visitedList

    print "can't find goal"
    return stop

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    print "test"
    from game import Directions
    # from util import PriorityQueue
    # South = Directions.SOUTH
    # West = Directions.WEST
    # East = Directions.EAST
    # North = Directions.NORTH
    stop = Directions.STOP

    # startNode = problem.getStartState()
    # pQueue = PriorityQueue()
    # pQueue.push(startNode, 0)
    # ParentNodeOf = {}
    # cumCost = {}
    # ParentNodeOf[startNode] = None
    # cumCost[startNode] = 0

    # while not pQueue.isEmpty():
    #     currentNode = pQueue.pop()
    #     print currentNode

        # if problem.isGoalState(currentNode):
        # return stop

        # allCurrentSuccessor = problem.getSuccessors(currentNode)
        # for Node in allCurrentSuccessor:
        #     newCost = 


    return stop

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
