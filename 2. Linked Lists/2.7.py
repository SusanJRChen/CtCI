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
            node = diction[cur.data]
            potNode = node.next
        elif (potential):
            if (potNode == None):
                return node
            elif (cur.data != potNode.data):
                node = None
                potNode = None
                potential = False
            elif (cur.data == potNode.data):
                potNode = potNode.next
        cur = cur.next

    return node

a = Node(7)
a.insertList([5,7,6,1,7])
a.print()
print()
b = Node(3)
b.insertList([1,6,3,6,1,7])
b.print()
print()

c = interset(a,b)
c.print()
