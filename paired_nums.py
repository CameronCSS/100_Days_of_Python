target = 9

nums = [2, 7, 11, 15, 1, 8]

# Find all the pairs that add up to the target
def two_sum(nums, target):
    h = {}
    pairs = []
    
    for i, num in enumerate(nums):
        desired = target - num
        if desired in h:
            pairs.append((desired, num))
        h[num] = i

    return pairs
            
            
print(two_sum(nums, target))