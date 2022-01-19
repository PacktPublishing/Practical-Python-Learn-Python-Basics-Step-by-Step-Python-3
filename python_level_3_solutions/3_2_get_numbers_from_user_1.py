def compute_list_average(number_list):
    return sum(number_list) / len(number_list)

number_list = []

for i in range(5):
    number_list.append(float(input("Give a number: ")))

print(compute_list_average(number_list))