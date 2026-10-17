# def hashmap(nums):
#     hashset = set()
#     for i in nums:
#         if i in hashset:
#             return True
#         hashset.add(i)
#     return False


# print(hashmap("alga"))


def count(items):
    freq = {}

    for x in items:
        if x in freq:
            freq[x] += 1 
        else:
            freq[x] = 1
    return freq

print(count("algara"))
