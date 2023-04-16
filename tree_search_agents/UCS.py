"""
    Name: Esrah
    Surname: Zahid
    Student ID: S020289
"""

from tree_search_agents.TreeSearchAgent import *
from tree_search_agents.PriorityQueue import PriorityQueue
import time


class UCSAgent(TreeSearchAgent):
    def run(self, env: Environment) -> (List[int], float, list):
        """
            You should implement this method for Uniform Cost Search algorithm.

            DO NOT CHANGE the name, parameters and output of the method.
        :param env: Environment
        :return: List of actions and total score
        """
        # initialization step
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
                    prev_state, action, cost = path[current_state]
                    expansion.append((current_state, action, cost))
                    current_state = prev_state
                directions, actions, cost = zip(*expansion)
                action_list = list(actions)[::-1]
                total_score = sum(list(cost))
                # print(f'Max Nodes Visited: {len(visited)}')
                return action_list, total_score, list(visited.keys())
            else:
                for action in range(4):
                    next_state, reward, done = env.move(action)
                    cumulative_cost = reward + current_reward
                    env.set_current_state(current_state)
                    if current_state != next_state:
                        if next_state not in visited or cumulative_cost > visited[next_state]:
                            queue.enqueue(next_state, cumulative_cost)
                            visited[next_state] = cumulative_cost
                            if next_state not in path:
                                path[next_state] = (current_state, action, reward)
        return [], 0., []

    @property
    def name(self) -> str:
        return "UCS"
