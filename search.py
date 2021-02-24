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

## Completed parts are done by:
@Author: Gayda Mutahar
@Date: 2019-09-02
@Description: Project 1 for the subject : AI Planning for Autonomy (COMP90054) @unimelb
"""

import util
from util import Stack
from util import Queue 
from util import PriorityQueue
#import node


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
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))"""
    
    dfsStack = Stack()
    visitedStates = []
    startState= problem.getStartState()   
    dfsStack.push((startState, []))

    while not dfsStack.isEmpty() and not problem.isGoalState(startState) :
        currNode, plan = dfsStack.pop()
        if currNode not in visitedStates:
            visitedStates.append(currNode)

            if problem.isGoalState(currNode):
                return plan
            child = problem.getSuccessors(currNode)

            for nextChild, action, cost in child:
                dfsStack.push((nextChild, plan + [action]))

 
def breadthFirstSearch(problem):
       
    bfsQueue = Queue()
    visitedStates = []
    startState= problem.getStartState()   
    bfsQueue.push((startState, []))

    while not bfsQueue.isEmpty() and not problem.isGoalState(startState) :
        currNode, plan = bfsQueue.pop()
        if currNode not in visitedStates:
            visitedStates.append(currNode)

            if problem.isGoalState(currNode):
                return plan
            child = problem.getSuccessors(currNode)

            for nextChild, action, cost in child:
                bfsQueue.push((nextChild, plan + [action]))
            
    util.raiseNotDefined()
    
    """Search the shallowest nodes in the search tree first.""" 
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"""
   
    # following the slid's algrothim
    PriorityQ = PriorityQueue() #open states list
    visitedState = [] #closed visited list 
    startState= problem.getStartState()   
    if problem.isGoalState(startState):#check if the start state is the goal state or not
        return []
    #bestg =[]
    PriorityQ.push((startState,[],0),0)
                  
    while not PriorityQ.isEmpty():        
        currNode, plan, gCost= PriorityQ.pop()   
            
        if currNode not in visitedState: #check duplicates
             visitedState.append(currNode) #close state
             
             if problem.isGoalState(currNode):
                return (plan)  
                    
             child = problem.getSuccessors(currNode)
                         
             for nextchild, action, cost in child: #expand state
                 if nextchild not in visitedState:
                    PriorityQ.push((nextchild, plan + [action], gCost+cost), gCost + cost + heuristic(nextchild,problem))             
    else:
        return False   
                       
    util.raiseNotDefined()
 
  
def iterativeDeepeningSearch(problem):
    idQueue = Queue ()     
    startState= problem.getStartState()
    maxDepth = 1; #intiate a depth limit 
    
    while True: #repeat always until reaching the goal 
        
        visitedState = []
        idQueue.push((startState,[],0)) #add the start state to the open list 
        
        currNode,plan,gCost = idQueue.pop() 
        if currNode not in visitedState: #check duplicates
            visitedState.append(currNode) #close state
        
        for depth in range(0, maxDepth) : 
            if problem.isGoalState(currNode):
                break
            else:
               
               child = problem.getSuccessors(currNode)
               for nextChild in child:
               
                   if (nextChild[0] not in visitedState):                   
                      idQueue.push((nextChild[0],plan + [nextChild[1]],gCost + nextChild[2])) 
                      visitedState.append(nextChild[0]) # add this node to visited states list(closed List) 
                    
               if idQueue.isEmpty():
                  break;
     
               currNode,plan,gCost = idQueue.pop()
               depth = depth-1
                            
        if problem.isGoalState(currNode):
           return (plan)
                 
        maxDepth += 1 # increase the depth
  
    util.raiseNotDefined()
                                  
                
  
def waStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has has the weighted (x 2) lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE FOR TASK 2 ***"
   # following the slid's algrothim
    PriorityQ = PriorityQueue() #open states list
    visitedState = [] #closed visited list 
    startState= problem.getStartState()   
    if problem.isGoalState(startState):#check if the start state is the goal state or not
        return []
    #bestg =[]
    PriorityQ.push((startState,[],0),0 +(2* heuristic(problem.getStartState(),problem))) #add the start state to the open states list
         
    while not PriorityQ.isEmpty():        
        currNode, plan, gCost= PriorityQ.pop()   
            
        if currNode not in visitedState: #check duplicates
            visitedState.append(currNode) #close state
             
            if problem.isGoalState(currNode):
                return (plan)  
             
            child = problem.getSuccessors(currNode)
             
            for nextchild, action, cost in child:#expand state
               #  tCost= gCost + nextchild [1]
                if (nextchild[0] not in visitedState) :
                    PriorityQ.push((nextchild, plan + [action], gCost+cost), gCost + cost +(2* heuristic(nextchild,problem)))              
    else:
        return False 
    util.raiseNotDefined()
  
   
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
wastar = waStarSearch
