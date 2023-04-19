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
        visited = {start_state: 0}  # stores every node that was visited with its cost (score + heuristic)
        expansion = []   # stores every node that was expanded in path
        path = {}   # stores how to retrace the path steps by storing how to get from one path to another
        total_score = 0   # stores the total cost to end goal
        while not queue.is_empty():
            current_reward = queue.queue[0][1]
            current_state = queue.dequeue()
            env.set_current_state(current_state)
            if current_state in goal_states:
                while current_state != start_state:
                    prev_state, action, cost = path[current_state]
                    expansion.append((current_state, action, cost))
                    total_score += cost
                    current_state = prev_state
                directions, actions, cost = zip(*expansion)
                action_list = list(actions)[::-1]
                return action_list, total_score, list(visited.keys())
            else:
                for action in range(4):
                    next_state, reward, done = env.move(action)
                    env.set_current_state(current_state)
                    if current_state != next_state:
                        cumulative_cost = reward + current_reward
                        heuristic_value = self.get_heuristic(env,
                                                             next_state,
                                                             goal_positions=goal_states,
                                                             heuristic_type='manhattan')
                        total_cost = cumulative_cost - heuristic_value
                        if next_state not in visited or total_cost > visited[next_state]:
                            queue.enqueue(next_state, total_cost)
                            visited[next_state] = cumulative_cost
                            if next_state not in path:
                                path[next_state] = (current_state, action, reward)

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
        goal_positions = kwargs.get('goal_positions', [])
        heuristic_type = kwargs.get('heuristic_type', 'manhattan')
        if heuristic_type == 'manhattan':
            min_distance = min(
                abs(x1 - x2) + abs(y1 - y2)
                for goal_position in goal_positions
                for (x1, y1), (x2, y2) in [(current_position, env.to_position(goal_position))]
            )
        elif heuristic_type == 'euclidean':
            min_distance = min(
                numpy.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                for goal_position in goal_positions
                for (x1, y1), (x2, y2) in [(current_position, env.to_position(goal_position))]
            )
        else:
            raise ValueError("Invalid heuristic_type. Allowed values are 'manhattan' and 'euclidean'.")

        return min_distance

    @property
    def name(self) -> str:
        return "AStar"
