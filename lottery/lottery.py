from random import randint
def generate_numbers(n):
    """번호 뽑기"""
    number_list = []
    for i in range(1, n + 1):
        select_num = randint(1, 45)
        if select_num not in number_list:
            number_list.append(select_num)
    return number_list


def draw_winning_numbers():
    """당첨 번호 뽑기"""
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(numbers, winning_numbers):
    """겹치는 번호 개수"""
    cnt = 0
    for i in numbers:
        if i in winning_numbers:
           cnt += 1
    return cnt

def check(numbers, winning_numbers):
    """당첨 확인"""
    nums_cnt = count_matching_numbers(numbers, winning_numbers[:6])
    if nums_cnt == 6:
        return 1000000000
    elif nums_cnt == 5 and winning_numbers[6] in numbers:
        return 50000000
    elif nums_cnt == 5:
        return 1000000
    elif nums_cnt == 4:
        return 50000
    elif nums_cnt == 3:
        return 5000
    else:
        return 0