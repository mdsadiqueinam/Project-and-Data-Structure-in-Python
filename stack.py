import LinkedList

class MyStack:
    def __init__(self) -> None:
        self.container = LinkedList.LinkedList()

    def push(self, data):
        self.container.insertAtBegining(data)
    
    def front(self):
        if self.isEmpty():
            print("Error: the stack is empty")
        else:
            return self.container.head.data

    def pop(self):
        if self.isEmpty():
            print("Error: can't pop from an empty stack")
        else:
            self.container.deleteNode(self.container.head)

    def isEmpty(self) -> bool:
        if self.container.__len__()==0:
            return True
        return False

    def __len__(self):
        return self.container.__len__()

    def __str__(self) -> str:
        return "MyStack("+self.container.__str__()+")"

if __name__=="__main__":
    m= MyStack()
    m.push(10)
    m.push(20)
    print(m)
    print(m.front())
    m.pop()
    print(m.front())
    m.pop()
    print(m.front())
    m.pop()
