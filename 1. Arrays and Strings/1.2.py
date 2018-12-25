word1 = input("word 1: ")
word2 = input("word 2: ")

def checkPermutation(word1, word2):
    diction = {}

    for i in word1:
        if i in diction:
            diction[i] += 1
        else:
            diction[i] = 1
    
    for i in word2:
        if i in diction:
            if diction[i] == 1:
                del diction[i]
            else:
                diction[i] -= 1
        else:
            return False
            
    if diction == {}:
        return True
    else:
        return False

print(checkPermutation(word1, word2))