import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st option
n = random.randint(0, len(friends)-1)

print(friends[n])

# 2nd option
print(random.choice(friends))