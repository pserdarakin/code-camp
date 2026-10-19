# Write binary_search(nums, target): return the index of target in a sorted list, or -1 if it is not there.

# Integer -> Integer

# [1 2 3 4 5 6 7 8 9 10] 9 => I ll go into middle which will be half of the == len(nums)/2, i need two indices == left and right so i can use in loop
# -^--------^---------^
#  L        M         R   Target > M so L == M  
#           L    M    R   Target > M so L == M
#                L M. R   

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    return -1

print(binary_search([2, 4, 5, 9, 10, 20, 30], 20))        

