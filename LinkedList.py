
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __findParentNode(self, Index=None, Data=None):
        root = self.head
        c = 0
        while (Index != None and root != None and c < Index-1) or (Data != None and root.next != None and root.next.data != Data):
            root = root.next
            c += 1
        return root

    def __deleteByroot(self, root: Node):
        if root.next != self.tail:
            self.deleteNode(root.next)
        else:
            root.next = None
            self.tail = root
            self.size -= 1

    def insertAtBegining(self, x) -> None:
        self.size += 1
        temp = Node(x, self.head)
        self.head = temp
        if self.tail == None:
            self.tail = self.head

    def insertAtEnd(self, data) -> None:
        self.size += 1
        if(self.head == None):
            self.insertAtBegining(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def insertAtIndex(self, data, index) -> None:
        if index == 0:
            self.insertAtBegining(data)
        elif index == self.size:
            self.insertAtEnd(data)
        elif index < 0 or index > self.size:
            print(
                "Error: Invalid index number {} please input correct index".format(index))
        else:
            self.size += 1
            root = self.__findParentNode(Index=index)
            temp = root.next
            root.next = Node(data, temp)

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            print(
                "Error: Invalid index number {} please input correct index".format(index))
        elif index == 0:
            self.deleteNode(self.head)
        else:
            root = self.__findParentNode(Index=index)
            self.__deleteByroot(root)

    def deleteData(self, data):
        if self.head == None:
            print("Error: LinkedList is empty")
        else:
            if data == self.head.data:
                self.deleteNode(self.head)
            else:
                root = self.__findParentNode(Data=data)
                if root.next == None:
                    print("Data {} doesn't exist in the linked list".format(data))
                else:
                    self.__deleteByroot(root)

    def deleteNode(self, curr_node: Node):
        if curr_node != self.tail:
            curr_node.data = curr_node.next.data
            curr_node.next = curr_node.next.next
            self.size -= 1
        else:
            self.deleteData(curr_node.data)

    def __str__(self) -> str:
        string = []
        root = self.head
        while(root != None):
            string.append(str(root.data))
            root = root.next
        return " -> ".join(string)

    def __len__(self):
        return self.size


if __name__ == "__main__":
    l = LinkedList()
    l.insertAtBegining(20)
    l.insertAtEnd(30)
    l.insertAtBegining(10)
    l.insertAtIndex(5, 3)
    l.insertAtIndex(2, 3)
    l.insertAtIndex(1, 2)
    print(l)
    print(len(l))
    l.deleteData(2)
    print(l)
    print(len(l))
