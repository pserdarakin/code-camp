def count(items):
    freq = {}
    for count in items:
        if count in freq:
            freq[count] += 1
        else:
            freq[count] = 1
    return freq


print(count("anagram"))