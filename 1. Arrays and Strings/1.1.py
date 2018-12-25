word = input("unique word?: ")
notunique = False

diction = {}
for i in word:
    if (i in diction):
        print("not unique")
        notunique = True
    else:
        diction[i] = 1

if(not notunique): print("unique")