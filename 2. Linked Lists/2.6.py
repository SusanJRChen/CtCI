from LinkedList import * 

def isPalindrome(node):
    diction = {}
    cur = node
    count = 0

    while(cur != None):
        diction[count] = cur
        cur = cur.next
        count += 1
    for i in range(int((count)/2)):
        if (diction[i].data != diction[count - 1 - i].data):
            return False

    return True

a = Node(7)
a.insertList([1,6,7,6,1,7])
a.print()
print(isPalindrome(a))
