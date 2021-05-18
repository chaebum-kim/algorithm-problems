''' Question: 모의고사
** https://programmers.co.kr/learn/courses/30/lessons/42840
'''


def solution(answers):
    plans = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    counts = []

    for plan in plans:
        counts.append(grade(answers, plan))

    answer = []
    max_ = max(counts)
    answer = [i + 1 for i, count in enumerate(counts) if count == max_]

    return answer


def grade(answers, plan):
    count = 0
    len_plan = len(plan)
    for i in range(len(answers)):
        if answers[i] == plan[i % len_plan]:
            count += 1
    return count
