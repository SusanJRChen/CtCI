from LinkedList import *

def kthToLast(node, k):
    diction = {}
    cur = node
    counter = 0

    while cur != None:
        diction[counter] = cur
        cur = cur.next
        counter += 1
    
    return diction[counter-k]

a = Node(1)
a.insertList([5,2,3,4,15,4,5])
a.print()
print(",")
a = kthToLast(a, 3)
a.print()