from LinkedList import * 

def delMiddle(node):
    diction = {}
    cur = node
    counter = 1

    while cur != None:
        diction[counter] = cur
        cur = cur.next
        counter += 1

    if counter % 2 == 0:
        return node
    else:
        delnum = int(counter/2) - 1
        diction[delnum].next = diction[delnum].next.next
        return node

a = Node(1)
a.insertList([5,2,3,4,15,4,5])
a.print()
print()
a = delMiddle(a)
a.print()