''' Question: 체육복
*   https://programmers.co.kr/learn/courses/30/lessons/42862
'''


def solution(n, lost, reserve):

    lost_ = list(set(lost) - set(reserve))
    reserve_ = list(set(reserve)-set(lost))
    attendees = n - len(lost_)

    reserve_.sort(reverse=True)

    for borrower in lost_:
        for lender in reserve_:
            if borrower + 1 == lender or borrower - 1 == lender:
                attendees += 1
                reserve_.remove(lender)
                break

    return attendees
