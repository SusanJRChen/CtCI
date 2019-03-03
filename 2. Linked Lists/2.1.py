from LinkedList import * 
    
def removeDuplicate(node, dup={}):
    if node.data in dup:
        if node.next == None:
            node.prev.next = None
            return None
        node.next.prev = node.prev
        node.prev.next = node.next
        return node.next
    else:
        dup[node.data] = True
    rest = removeDuplicate(node.next, dup)
    node.next = rest
    if rest != None:
        rest.prev = node
    return node

a = Node(1)
a.insertList([5,2,3,4,15,4,5])
a.print()
print(",")
a = removeDuplicate(a)
a.print()