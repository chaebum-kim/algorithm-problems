''' Question: 더 맵게
*   https://programmers.co.kr/learn/courses/30/lessons/42626
'''

import heapq


# min-heap
def solution(scoville, K):

    answer = 0
    heapq.heapify(scoville)

    while scoville:
        current = heapq.heappop(scoville)
        if current < K:
            if scoville:
                next_ = heapq.heappop(scoville)
                new = current + next_*2
                heapq.heappush(scoville, new)
                answer += 1
            else:
                return -1
        else:
            return answer
