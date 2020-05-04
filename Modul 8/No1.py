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
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

def cetakHexa(a):
    hexa = Stack()
    if a == 0: hexa.push(0);
    while a != 0:
        if a % 16 == 10:
            mod = 'A'
        elif a % 16 == 11:
            mod = 'B'
        elif a % 16 == 12:
            mod = 'C'
        elif a % 16 == 13:
            mod = 'D'
        elif a % 16 == 14:
            mod = 'E'
        elif a % 16 == 15:
            mod = 'F'
        else:
            mod = a % 16
        a = a // 16
        hexa.push(mod)
    string = ""
    for i in range(len(hexa)):
      string = string + str(hexa.pop())
    return string
