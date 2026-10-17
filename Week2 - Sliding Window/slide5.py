def longest_at_most(nums, k):

    window_sum = 0
    left = 0
    best = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > k:
            window_sum -= nums[left]
            left += 1
            best = max(best, right - left + 1)

    return best

print(longest_at_most([2,1,3,1,1,4],5))