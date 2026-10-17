def longest_at_most(nums,k):
    # [2 1 5 1 3 2] 3 
    left = 0
    window_sum = 0
    max_length = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > k and left <=right:
            window_sum -= nums[left]
            left += 1
            max_length = max(max_length, right - left + 1)
    return max_length



print(longest_at_most([2, 1, 3, 1, 1, 4], 5)) 




# First, I define the function longest_at_most accepting the array nums and target k. 
# I initialize left, window_sum, and max_length to 0 
# to track the starting index of the window, the running sum of the numbers inside it, 
# and the longest valid window seen so far. 
# Then, I loop through the array using right as the index from 0 to the end of nums. 
# Inside the loop, I expand my window by adding nums[right] to window_sum. 
# Immediately after, I check if window_sum is greater than k (while making sure left <= right); 
# if it is, I enter a while loop to shrink the window from the left by subtracting nums[left] 
# from window_sum and moving left forward by 1, repeating this until the sum is at most k. 
# Once the window is valid again, I calculate the current window size as right - left + 1 and 
# update max_length to hold the maximum between the previous max_length and this new size. 
# Finally, once the for loop finishes checking every index, I return max_length.