numbers = [1,1,1,1,1]
target = 3
result = []
target_count = 0
def get_count_of_ways_to_target_by_doing_plus_or_minus(array,current_index, current_sum, target_number):
    if current_index == len(array):
        if current_sum == target_number:
            global target_count
            target_count+= 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index], target_number)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index], target_number)

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, 0, 0, target))
print(target_count)



# print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!