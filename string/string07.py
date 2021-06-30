''' Question: 뉴스 클러스터링
*   https://programmers.co.kr/learn/courses/30/lessons/17677 
'''


def solution(str1, str2):

    set1, set2 = [], []
    n1, n2 = len(str1), len(str2)
    set1 = [str1[i:i+2].lower() for i in range(n1-1) if str1[i:i+2].isalpha()]
    set2 = [str2[i:i+2].lower() for i in range(n2-1) if str2[i:i+2].isalpha()]

    sum_ = len(set1) + len(set2)

    intersection = 0
    for e in set1:
        if e in set2:
            intersection += 1
            set2.remove(e)

    union = sum_ - intersection

    j = 1 if union == 0 else intersection / union

    return int(j * 65536)
