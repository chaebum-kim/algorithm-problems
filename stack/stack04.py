''' Question: 주식가격
*   https://programmers.co.kr/learn/courses/30/lessons/42584
'''


# Brute force solution
def solution(prices):

    result = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                break
        result.append(j-i)

    return result

# Time complexity: O(N^2)
# Space complexity: O(N)
