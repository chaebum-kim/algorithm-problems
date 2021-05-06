''' Question: 디스크 컨트롤러
** https://programmers.co.kr/learn/courses/30/lessons/42627
'''

import heapq as hq


def solution(jobs):
    def push_waiting(last, now, jobs, waiting):
        for i, job in enumerate(jobs):
            time, cost = job
            if last < time <= now:
                hq.heappush(waiting, ((cost, time), i))

    answer, now, count = 0, 0, 0
    last = -1
    waiting = []
    hq.heapify(waiting)

    while count < len(jobs):
        push_waiting(last, now, jobs, waiting)
        if waiting:
            prior, i = hq.heappop(waiting)
            time, cost = jobs[i]
            last = now
            now += cost
            answer += (now - time)
            count += 1
        else:
            now += 1

    return int(answer / length)
