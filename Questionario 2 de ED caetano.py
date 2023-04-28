class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)
      
    def pop(self):
        if self.items != []:
            return self.items.pop(0)
        else:
            pass 
    def peek(self):
        for i in range(len(self.items)):
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack() 
s.push(1)
s.push(2)
s.pop()
s.pop()
s.pop()
s.push(42)
while not s.isEmpty():
    print(s.pop())
