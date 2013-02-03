from scipy import *
import sys, time

from pybrain.rl.environments.mazes import Maze, MDPMazeTask
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.experiments import Experiment
from pybrain.rl.environments import Task

import pylab
pylab.gray()
pylab.ion()

d = dict()
s1 = "a"
s2 = "b"
s3 = "c"
d[s1] = 1
d[s2] = 2
d[s3] = 3

d[1] = s1
d[2] = s2
d[3] = s3

structure = array([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [d[s1], 0, 0, 1, 0, 0, 0, 0, 3],
                   [3, 0, 0, 1, 0, 0, 1, 0, 2],
                   [1, 0, 0, d[s2], 0, 0, 3, 0, 1],
                   [1, 0, 0, 2, 0, 1, 2, 0, 1],
                   [1, 0, 0, 0, 0, 0, 3, 0, 2],
                   [1, 1, 2, 3, 2, 3, 2, 0, 3],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 2, 1, 2, 1, 2, 1, 3]])


controller = ActionValueTable(81, 4)
controller.initialize(1.)

learner = Q()
agent = LearningAgent(controller, learner)

environment = Maze(structure, (7, 7))
task = MDPMazeTask(environment)

experiment = Experiment(task, agent)

while True:
    experiment.doInteractions(100)
    agent.learn()
    agent.reset()
    print agent.history
    pylab.pcolor(controller.params.reshape(81,4).max(1).reshape(9,9))
    pylab.draw()