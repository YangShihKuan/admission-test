def find_max(numbers):
    max_num = 0
    for temp_num in numbers:
        if temp_num > max_num:
            max_num = temp_num
    return max_num


def find_position(numbers, target):
    target_index = -1
    for temp_ind, temp_tar in enumerate(numbers):
        if temp_tar == target:
            target_index = temp_ind
            break
    return target_index


print(find_max([1, 2, 4, 5]))  # should print 5
print(find_max([5, 2, 7, 1, 6]))  # should print 7
print(find_position([5, 2, 7, 1, 6], 5))  # should print 0
print(find_position([5, 2, 7, 1, 6], 7))  # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))  # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8))  # should print -1
