from LinkedList import * 

def sumLists(l1, l2):
    cur1 = l1
    cur2 = l2
    sumlist = None
    carryover = 0

    while (cur1 != None and cur2 != None):
        digit = cur1.data + cur2.data + carryover
        carryover = 0
        if digit >= 10:
            carryover = 1
            digit -= 10
        if sumlist == None:
            sumlist = Node(digit)
        else:
            sumlist.insert(digit)
        
        cur1 = cur1.next
        cur2 = cur2.next
    
    if carryover > 0:
        sumlist.insert(carryover)
    
    return sumlist

a = Node(7)
a.insertList([1,6])
a.print()
print()
b = Node(5)
b.insertList([9,5])
b.print()
print()
sumLists(a,b).print()