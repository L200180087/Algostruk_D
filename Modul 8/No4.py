class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)

    #4.1
    def getFrontMost(self):
        return self.qlist[0]

    #4.2
    def getRearMost(self):
        return self.qlist[len(self.qlist) - 1]

kyu = Queue()
kyu.enqueue(3)
kyu.enqueue(6)
kyu.enqueue(9)
kyu.enqueue(12)
kyu.enqueue(15)
kyu.enqueue(18)

print("Queue :", kyu.qlist)

print("Terdepan :", kyu.getFrontMost())
print("Terbelakang :", kyu.getRearMost())
