seat_count = 9
vip_seat_array = [4, 7]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4와 7이 고정되어 있을때, 만들 수 있는 여러 좌석의 개수
# 1 2 3
# 5 6
# 8 9

# 좌석 [1,2] 2
# [1,2] [2,1]
# 좌석 [1,2,3] 3
# [2,1,3] [1,3,2] [1,2,3]
# 좌석 [1,2,3,4] 5
# [1,2,3,4] [1,3,2,4] [1,2,4,3] [2,1,3,4] [2,1,4,3]
# 좌석 [1,2,3,4,5] 8
# [1,2,3,4,5] [1,2,3,5,4] [2,1,3,4,5]
# [2,1,3,5,4] [1,2,4,3,5] [2,1,4,3,5]
# [2,1,3,4,5] [1,3,2,4,5]

memo = {
    1: 1,
    2: 2
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1
    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))