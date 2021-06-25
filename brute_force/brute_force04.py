''' Question: 문자열 압축
*   https://programmers.co.kr/learn/courses/30/lessons/60057
'''


def solution(s):

    minlen = 0
    N = len(s)

    for length in range(1, N+1):
        compressed = ''
        standard = s[:length]
        count, i = 0, 0

        while i < N:
            while i < N and s[i:i+length] == standard:
                count += 1
                i += length

            if count > 1:
                compressed += str(count)
            compressed += standard

            count = 0
            standard = s[i:i+length]

        if (n := len(compressed)) < minlen or minlen == 0:
            minlen = n

    return minlen
