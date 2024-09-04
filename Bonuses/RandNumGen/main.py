import random

lower_bound = int(input("Enter lowest possible number: "))
upper_bound = int(input("Enter highest possible number: "))


random_number = random.randint(lower_bound, upper_bound)

print(random_number)