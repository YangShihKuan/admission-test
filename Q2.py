def count(input):
    count_dict = {}
    count_key = count_dict.keys()
    for i in input:
        if i not in count_key:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    return count_dict


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    group_dict = {}
    group_key = group_dict.keys()
    for temp_dict in input:
        temp_key = temp_dict['key']
        temp_value = temp_dict['value']
        if temp_key not in group_key:
            group_dict[temp_key] = temp_value
        else:
            group_dict[temp_key] += temp_value
    return group_dict


input2 = [{'key': 'a', 'value': 3},
          {'key': 'b', 'value': 1},
          {'key': 'c', 'value': 2},
          {'key': 'a', 'value': 3},
          {'key': 'c', 'value': 5}]
print(group_by_key(input2))  # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
