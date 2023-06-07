top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)

random_numbers = [2, 6,5,8,4,9,-3]
random_numbers.sort()
print(random_numbers)

random_numbers = [2, 6,5,8,4,9,-3]
random_numbers.sort(reverse=True)
print(random_numbers)

top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)