def compute_max_value_from_list(number_list):
    max_value = 0
    for number in number_list:
        if number > max_value:
            max_value = number
    return max_value

number_list = [3, 2, -3, 9, 4]
max_value = compute_max_value_from_list(number_list)
print(max_value)