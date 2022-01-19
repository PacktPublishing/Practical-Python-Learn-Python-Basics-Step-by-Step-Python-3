from my_computations import compute_list_average

number_list = []

with open("file_test", "r") as f:
    for line in f:
        number_list.append(float(line.rstrip("\n")))

print(number_list)
print(compute_list_average(number_list))
