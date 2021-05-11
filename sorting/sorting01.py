''' Question: K번째 수
*   https://programmers.co.kr/learn/courses/30/lessons/42748
'''


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        subarray = array[i-1:j]
        subarray.sort()
        answer.append(subarray[k-1])
    return answer
