class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        n = []
        for i in self.qlist:
            n.append(i.priority)
        print (self.qlist.pop(n.index(min(n))).item)

    def tampil(self) :
        print(self.qlist)

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority


kyu = PriorityQueue()
kyu.enqueue('Nomer 3', 3)
kyu.enqueue('Nomer 1', 1)
kyu.enqueue('Nomer 4', 4)
kyu.enqueue('Nomer 5', 5)
kyu.enqueue('Nomer 2', 2)

