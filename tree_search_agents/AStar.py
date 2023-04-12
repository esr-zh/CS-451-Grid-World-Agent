"""
    Name: Esrah
    Surname: Zahid
    Student ID: S020289
"""


from tree_search_agents.TreeSearchAgent import *
from tree_search_agents.PriorityQueue import PriorityQueue
import time


class AStarAgent(TreeSearchAgent):
    def run(self, env: Environment) -> (List[int], float, list):
        """
            You should implement this method for A* algorithm.

            DO NOT CHANGE the name, parameters and output of the method.
        :param env: Environment
        :return: List of actions and total score
        """

        return [], 0., []

    def get_heuristic(self, env: Environment, state: int, **kwargs) -> float:
        """
            You should implement your heuristic calculation for A*

            DO NOT CHANGE the name, parameters and output of the method.

            Note that you can use kwargs to get more parameters :)
        :param env: Environment object
        :param state: Current state
        :param kwargs: More parameters
        :return: Heuristic score
        """

        return 0.

    @property
    def name(self) -> str:
        return "AStar"
