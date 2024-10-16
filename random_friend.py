import random

# Pick a random friend
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

rand_num = random.randint(0,4)

print(friends[rand_num])


# Another way to do this
print(random.choice(friends))