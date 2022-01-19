city_list = []

with open("unordered_cities.txt", "r") as f:
    for line in f:
        city_list.append(line.rstrip("\n"))

sorted_city_list = sorted(city_list)

with open("ordered_cities.txt", "w") as f:
    for city in sorted_city_list:
        f.write(city + "\n")

print("done")