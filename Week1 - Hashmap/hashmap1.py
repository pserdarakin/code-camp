def count(items):

    seen = {}

    for i in items:
        if i in seen:
            seen[i] = 1 + seen[i]
        else:
            seen[i] = 1
    return seen

print(count("anagram"))

    