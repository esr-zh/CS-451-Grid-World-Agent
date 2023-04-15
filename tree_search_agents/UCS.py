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

        start_state = env.reset()
        start_position = env.starting_position
        goal_states = env.get_goals()

        queue = PriorityQueue()
        explored = set()
        visited = {start_state: 0}
        path = {}
        queue.enqueue(start_state, 0)  # inserting start state into the priority queue
        # print(f'Queue: {queue.queue[0][0]}')
        actions = []
        total_cost = 0
        count = 0
        while not queue.is_empty():  # repeat till queue is not empty:
            current_reward = queue.queue[0][1]
            current_state = queue.dequeue()  # remove element with the highest priority from queue
            current_position = env.to_position(current_state)
            print(current_position)

            if current_state in goal_states:  # If the node is a destination node, then exit
                print("Break happened!")
                break
            else:
                for action in range(4):
                    next_state, reward, done = env.move(action)
                    cumulative_cost = reward + current_reward
                    print(f'{env.to_position(next_state)}, {reward}, {done}')
                    if next_state not in visited or cumulative_cost < visited[next_state]:
                        queue.enqueue(next_state, cumulative_cost)
                        visited[next_state] = cumulative_cost
                        if next_state not in path:
                            path[next_state] = current_state, action
                        if done:
                            env.reset()
                            print("Done")
                        else:
                            env.set_current_state(current_state)
                            print(f'new position: {current_position}')
                            print(visited)
            count+=10
            if count == 20:
                break
        return [], 0., []

    @property
    def name(self) -> str:
        return "UCS"
