''' Question: 오픈채팅팡
*   https://programmers.co.kr/learn/courses/30/lessons/42888
'''


def solution(record):

    nicknames = {}
    messages = []
    IN, OUT = 1, 0

    for r in record:
        words = r.split()
        if words[0] in ("Enter", "Change"):
            nicknames[words[1]] = words[2]
        if words[0] == "Enter":
            messages.append((words[1], IN))
        elif words[0] == "Leave":
            messages.append((words[1], OUT))

    result = []
    for m in messages:
        if m[1] == IN:
            result.append(f'{nicknames[m[0]]}님이 들어왔습니다.')
        else:
            result.append(f'{nicknames[m[0]]}님이 나갔습니다.')

    return result
