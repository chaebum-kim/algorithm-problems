''' Question: 전화번호 목록
*   https://programmers.co.kr/learn/courses/30/lessons/42577
'''


def solution(phone_book):
    seen = set()
    for phone_number in phone_book:
        seen.add(phone_number)
    for phone_number in phone_book:
        prefix = ''
        for digit in phone_number:
            prefix += digit
            if prefix in seen and prefix != phone_number:
                return False
    return True

# Time complexity: O(N)
# Space complexity: O(N)
