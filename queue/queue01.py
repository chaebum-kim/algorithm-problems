''' Question: 다리를 지나는 트럭
*   https://programmers.co.kr/learn/courses/30/lessons/42583/
'''
from collections import deque


def solution(bridge_length, weight, truck_weights):

    passing = deque()
    waiting = deque(truck_weights)
    capacity = weight
    count = time = 0

    while True:
        time += 1
        if passing:
            truck, entry_time = passing[0]
            if time - entry_time == bridge_length:
                passing.popleft()
                capacity += truck
                count += 1

        if count == len(truck_weights):
            break

        if waiting and waiting[0] <= capacity:
            truck = waiting.popleft()
            passing.append([truck, time])
            capacity -= truck

    return time

# Time complexity: O(T) -- total time needed for all trucks to pass the bridge
# Space complexity: O(N)
