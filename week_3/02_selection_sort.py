input = [4, 6, 2, 9, 1]


def selection_sort(array):
    length = len(array)
    for i in range(length - 1):
        min_index = i
        # print(i)
        for j in range(length - i):
            print(i + j)
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!