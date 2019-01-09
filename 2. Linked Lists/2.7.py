from LinkedList import * 

def interset(a, b):    
    diction = {}
    cur = a
    count = 0

    while(cur != None):
        diction[cur.data] = cur
        cur = cur.next
        count += 1
    
    cur = b
    potential = False
    node = None
    potNode = None

    while(cur != None):
        if (not potential and cur.data in diction):
            potential = True
            node = cur
            potNode = node
        elif (potential):
            potNode = potNode.next
        elif (potential and cur.next != None and potNode.next != None and cur.next.data != potNode.next.data):
            node = None
            potNode = None
            potential = False
        cur = cur.next

    return node

a = Node(7)
a.insertList([1,6,7,6,1,7])
a.print()
print()
b = Node(7)
b.insertList([1,6,3,6,1,7])
b.print()
print()

c = interset(a,b)
c.print()
