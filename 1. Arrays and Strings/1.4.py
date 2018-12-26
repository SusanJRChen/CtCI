

def palindromePermutation(word):
    newword = ""
    pairs = []
    singles = []
    
    for i in word:
        if i != " ":
            if i not in singles:
                singles.append(i)
            else:
                pairs.append(i)
                singles.remove(i)

    if len(singles) > 1:
        return -1
    
    if len(singles) == 0:
        singles = [""]

    permutations = (len(singles) + len(pairs)) * singles
    index = 0

    for i in range(0, len(pairs)):
        for j in range(0, len(permutations)):
            num = i + j
            if num > len(pairs) - 1:
                num -= len(pairs) + 1
                
            permutations[j] = pairs[num] + permutations[j]
            permutations[j] = permutations[j] + pairs[num]
    
    return permutations

print(palindromePermutation("cat tac"))