import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# version 1
# add 1, because randrange doesn't include upper bound
rand = random.randrange(lower_bound, upper_bound + 1)

# version 2
# docs.python.org:
# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
# rand = random.randrange(lower_bound, upper_bound)

print(rand)
