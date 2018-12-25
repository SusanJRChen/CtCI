word = input("word: ")
length = input("length: ")

def URLify(word, length):
    word = word[0:int(length) + 1]
    last = 0
    final = ""
    
    for i in range (0,len(word)):
        if (word[i] == " "):
            final += (word[last:i])
            final += "%20"
            last = i+1
        elif (i == len(word)-1):
            final += word[last:len(word)]
    

    return final

print(URLify(word, length))

