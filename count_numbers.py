
# Identify unique values from a list of numbers and print how many times each value occurs.

# Example output: 
# 5: 3 times
# 3: 2 times
# 6 1 time
# 7: 1 time

num_list = [5,3,5,6,3,5,7]

count_dict = {}

for num in num_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
        
for num, count in count_dict.items():
    if count > 1:
        print(f"{num}: {count} times")
    else:
        print(f"{num}: {count} time")