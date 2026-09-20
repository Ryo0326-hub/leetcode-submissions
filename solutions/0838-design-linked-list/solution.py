class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head.next
        for i in range(index):
            current = current.next
        return current.val
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        left = self.head
        right = self.head.next

        left.next = new_node 
        new_node.prev = left
        new_node.next = right 
        right.prev = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        left = self.tail.prev 
        right = self.tail 

        right.prev = new_node
        new_node.next = right 
        new_node.prev = left
        left.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        new_node = Node(val)
        left = self.head 
        right = left.next
        for i in range(index):
            left = left.next
            right = right.next
        left.next = new_node
        new_node.prev = left 
        new_node.next = right 
        right.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return 
        current = self.head.next
        for i in range(index):
            current = current.next
        left = current.prev
        right = current.next
        left.next = right
        right.prev = left
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
