class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip."
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
        print(self.items.pop(), "popped")
        print("stack sekarang", self.items)

    def push(self, data):
        self.items.append(data)
        print(data, "pushed")
        print("stack sekarang",self.items)

nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
    elif i % 4 == 0:
        nilai.pop()
