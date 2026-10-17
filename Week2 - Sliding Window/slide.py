# Sliding window

# Task: Write longest_at_most(nums, k): the length of the longest run of neighbouring numbers whose sum is at most k. 
# All numbers are positive. 
# Grow the window on the right, and shrink it from the left when the sum gets too big.

# Check: end with print(longest_at_most([2, 1, 3, 1, 1, 4], 5)), which should print 3



def longest_at_most(nums, k):
    total = 0
    left = 0
    best = 0

    for right in range(len(nums)):
        total = total + nums[right]
        while total > k:
            total = total - nums[left]
            left += 1
        best = max(best, right - left + 1)
    return best

print(longest_at_most([2, 1, 3, 1, 1, 4], 5)) 