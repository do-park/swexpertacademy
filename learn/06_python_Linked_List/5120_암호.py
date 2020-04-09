class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node

        self.before = None
        self.current = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node
        self.tail.link = self.head.link
        self.num_of_data += 1

    def first(self):
        self.current = self.head.link
        self.before = self.tail
        return self.current.data

    def next(self):
        self.before = self.current
        self.current = self.current.link
        return self.current.data

    def insert(self, data):
        new_node = Node(data)
        self.before.link = new_node
        new_node.link = self.current
        self.current = new_node
        self.num_of_data += 1

    def func(self, M):
        for m in range(M):
            self.next()
        num = self.before.data + self.current.data
        self.insert(num)

    def result(self):
        myli = [self.first()]
        for i in range(self.num_of_data -1):
            myli.append(self.next())
        return ' '.join(map(str, myli[-1:-11:-1]))


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    myll = LinkedList()
    for i in map(int, input().split()):
        myll.append(i)
    myll.first()
    for k in range(K):
        myll.func(M)
    print(f'#{tc} {myll.result()}')