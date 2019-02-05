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
This file contains all of the agents that can be selected to control Pacman.  To
select an agent, use the '-p' option when running pacman.py.  Arguments can be
passed to your agent using '-a'.  For example, to load a SearchAgent that uses
depth first search (dfs), run the following command:

> python pacman.py -p SearchAgent -a fn=depthFirstSearch

"""

from game import Directions
from game import Agent
from game import Actions
import util
import time
import search
import random

# this is an example Agent
class GoWestAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP

# Part 1
# implement this
import random()
class RandomAgent(Agent):
    def __init__(self):
        # This is the constructor. You can initialize data here if you want.
        # You do not need to write anything here if you don't want to.
        pass

    def getAction(self, state):
	x = random.randint(1,5)
	Directs = ["NORTH","SOUTH","EAST","WEST"]
	if Directs[x-1] in state.getLegalPacmanActions():
		return Directs[x-1]
	else:
		return Directions.STOP

# Part 2
# implement this
class SurroundingAwareAgent(Agent):
    def __init__(self):      
        currentFood = state.getFood()
	currentCap = state.getCapsules()

    def getAction(self, state):
        DIRtoVEC = Actions.directionToVector(Directions.state)
	DIRtoVECfood = [DIRtoVEC[x]+currentFood[x],DIRtoVEC[y]+currentFood[y]
	DIRtoVECcap = [DIRtoVEC[x]+currentCap[x],DIRtoVEC[y]+currentCap[y]
	if DIRtoVECfood[x][y] == True:
        	return Directions.state
	else:
		return Directions.STOP

	if DIRtoVECcap[x][y] == True:
		return Directions.state
	else:
		return Directions.STOP
	