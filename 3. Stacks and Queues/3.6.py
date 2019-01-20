class Node:
    def __init__(self, value, animalType):
        self.next = None
        self.value = value
        self.type = animalType

class AnimalShelter:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value, animalType):
        if (self.head == None):
            self.head = Node(value, animalType)
            self.tail = self.head
        else:
            temp = Node(value, animalType)
            self.tail.next = temp
            self.tail = temp

    def dequeue(self):
        if (self.head != None):
            temp = self.head
            self.head = self.head.next
            if (self.head == None):
                self.tail = self.head
            return temp.value
        else:
            return None
    
    def dequeueType(self, animalType):
        temp = self.head
        prev = self.head

        if (temp == None):
            return None
        elif (temp.next == None):
            if temp.type == animalType:
                self.head = temp
                return temp.value
            else:
                return None
        
        while (temp != None):
            if temp.type == animalType:
                prev.next = temp.next
                if (temp.next == None):
                    self.tail = prev
                return temp.value
            prev = temp
            temp = temp.next
        
        return temp
    
    def dequeueDog(self):
        return self.dequeueType("dog")
    
    def dequeueCat(self):
        return self.dequeueType("cat")

a = AnimalShelter()
a.enqueue("bob1", "dog")
a.enqueue("kat3", "cat")
a.enqueue("bob2", "dog")
a.enqueue("bob3", "dog")
a.enqueue("bob4", "dog")
a.enqueue("bob5", "dog")
a.enqueue("kat2", "cat")
print(a.dequeue())
print(a.dequeueDog())
print(a.dequeueCat())
print(a.dequeueDog())