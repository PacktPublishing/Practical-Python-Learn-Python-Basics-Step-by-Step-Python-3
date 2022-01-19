def compute_list_average(number_list):
    return sum(number_list) / len(number_list)

number_list = []

ask_user_for_numbers = True

while ask_user_for_numbers:
    user_input = float(input("Choose a number: "))
    if user_input == 0.0:
        ask_user_for_numbers = False
    else:
        number_list.append(user_input)

print(compute_list_average(number_list))