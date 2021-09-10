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
from queue import PriorityQueue


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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(
        problem.getStartState()))

    stateStack = util.Stack()
    directionalAccumulationStack = util.Stack()
    visited = []

    if problem.isGoalState(problem.getStartState()):
        return []

    stateStack.push(problem.getStartState())
    directionalAccumulationStack.push([])

    while not stateStack.isEmpty():

        """Step 1. remove the node from the stack as well as the path we took to get there"""
        currentNode = stateStack.pop()
        answer = directionalAccumulationStack.pop()
        visited.append(currentNode)

        """We ask ourselves if our current node is the goal state. If it is we return answer and
        if not we continue"""
        if problem.isGoalState(currentNode):
            return answer

        """We now check the successors of the current node and add them to the stack for checking later"""
        for successor in problem.getSuccessors(currentNode):

            """Have we seen this node before?"""
            if successor[0] not in visited:
                stateStack.push(successor[0])
                updatedAnswerPath = answer + [successor[1]]
                directionalAccumulationStack.push(updatedAnswerPath)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    nodeQueue = util.Queue()
    visited = []
    answer = []

    if problem.isGoalState(problem.getStartState()):
        return []

    nodeQueue.push((problem.getStartState(), answer))

    while not nodeQueue.isEmpty():

        """Step 1. remove the node from the stack as well as the path we took to get there"""
        currentState = nodeQueue.pop()
        currentNode = currentState[0]
        currentAnswer = currentState[1]
        """visited.append(currentNode)"""

        """We ask ourselves if our current node is the goal state. If it is we return answer and
        if not we continue"""
        if problem.isGoalState(currentNode):
            return currentAnswer

        """We now check the successors of the current node and add them to the stack for checking later"""
        for successor, direction, cost in problem.getSuccessors(currentNode):

            """Have we seen this node before?"""
            if successor not in visited:
                updatedAnswerPath = currentAnswer + [direction]
                nodeQueue.push((successor, updatedAnswerPath))
                visited.append(successor)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    stateQueue = PriorityQueue()
    visited = []

    if problem.isGoalState(problem.getStartState()):
        return []

    answer = []
    startNode = (problem.getStartState(), answer, 0)
    stateQueue.put((0, startNode))

    while not stateQueue.empty():

        """Step 1. remove the node from the stack as well as the path we took to get there"""
        dequeueOutput = stateQueue.get()
        currentState = dequeueOutput[1]
        currentNode = currentState[0]
        answer = currentState[1]
        currentCost = currentState[2]
        visited.append(currentNode)

        """We ask ourselves if our current node is the goal state. If it is we return answer and
        if not we continue"""
        if problem.isGoalState(currentNode):
            return answer

        """We now check the successors of the current node and add them to the stack for checking later"""
        for successor, direction, cost in problem.getSuccessors(currentNode):

            """Have we seen this node before?"""
            if successor not in visited:
                updatedAnswerPath = answer + [direction]
                updatedCost = currentCost + cost
                stateQueue.put(
                    (updatedCost, (successor, updatedAnswerPath, updatedCost)))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    stateQueue = PriorityQueue()
    visited = []

    if problem.isGoalState(problem.getStartState()):
        return []

    answer = []
    startNode = (problem.getStartState(), answer, 0)
    stateQueue.put((0, startNode))

    while not stateQueue.empty():

        """Step 1. remove the node from the stack as well as the path we took to get there"""
        dequeueOutput = stateQueue.get()
        currentState = dequeueOutput[1]
        currentNode = currentState[0]
        answer = currentState[1]
        currentCost = currentState[2]
        visited.append(currentNode)

        """We ask ourselves if our current node is the goal state. If it is we return answer and
        if not we continue"""
        if problem.isGoalState(currentNode):
            return answer

        """We now check the successors of the current node and add them to the stack for checking later"""
        for successor, direction, cost in problem.getSuccessors(currentNode):

            """Have we seen this node before?"""
            if successor not in visited:
                updatedAnswerPath = answer + [direction]
                updatedF = currentCost + cost + heuristic(successor, problem)
                stateQueue.put(
                    (cost, (successor, updatedAnswerPath, updatedF)))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
