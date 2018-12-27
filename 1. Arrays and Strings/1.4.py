

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
        return False
    else: return True

print(palindromePermutation("cat tac"))