"""
    Name: Esrah
    Surname: Zahid
    Student ID: S020289
"""
import numpy

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
        queue = PriorityQueue()
        start_state = env.reset()
        queue.enqueue(start_state, 0)
        goal_states = env.get_goals()
        visited = {start_state: 0}
        expansion = []
        path = {}
        while not queue.is_empty():
            current_reward = queue.queue[0][1]
            current_state = queue.dequeue()
            env.set_current_state(current_state)
            if current_state in goal_states:
                while current_state != start_state:
                    prev_state, action = path[current_state]
                    expansion.append((current_state, action))
                    current_state = prev_state
                directions, actions = zip(*expansion)
                action_list = list(actions)[::-1]
                expansion_list = list(directions)[::-1]
                return action_list, current_reward, expansion_list
            else:
                for action in range(4):
                    next_state, reward, done = env.move(action)
                    cumulative_cost = reward + current_reward
                    env.set_current_state(current_state)
                    total_cost = cumulative_cost - self.get_heuristic(env, next_state)

                    if current_state != next_state:
                        if next_state not in visited or total_cost > visited[next_state]:
                            queue.enqueue(next_state, total_cost)
                            visited[next_state] = total_cost
                            if next_state not in path:
                                path[next_state] = (current_state, action)

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

        current_position = env.to_position(state)
        goal_positions = env.get_goals()
        distances = []
        for goal_position in goal_positions:
            position = env.to_position(goal_position)
            dx = abs(current_position[0] - position[0])
            dy = abs(current_position[1] - position[1])
            distances.append(dx + dy)

        # current_position = env.to_position(state)
        # goal_positions = env.get_goals()
        # distances = []
        # for goal_position in goal_positions:
        #     position = env.to_position(goal_position)
        #     dx = abs(current_position[0] - position[0])
        #     dy = abs(current_position[1] - position[1])
        #     distances.append(numpy.sqrt(dx ** 2 + dy ** 2))

        return min(distances)

    @property
    def name(self) -> str:
        return "AStar"
