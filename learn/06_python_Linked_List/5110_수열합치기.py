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
        self.num_of_data += 1

    def first(self):
        if not self.num_of_data:
            return None
        self.before = self.head
        self.current = self.head.link
        return self.current.data

    def next(self):
        self.before = self.current
        self.current = self.current.link
        if self.current is None:
            return None
        return self.current.data

    def insert(self, new_list):
        insert_num = new_list.first()
        num = self.first()
        for i in range(self.num_of_data):
            if num > insert_num:
                self.before.link = new_list.head.link
                new_list.tail.link = self.current
                self.num_of_data += new_list.num_of_data
                break
            num = self.next()
        else:
            self.tail.link = new_list.head.link
            self.num_of_data += new_list.num_of_data

    def result(self):
        myli = []
        num = self.first()
        for i in range(self.num_of_data):
            myli.append(num)
            num = self.next()
        return ' '.join(map(str, myli[-1:-11:-1]))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    myll = LinkedList()
    for i in map(int, input().split()):
        myll.append(i)
    for m in range(M - 1):
        temp = LinkedList()
        for i in map(int, input().split()):
            temp.append(i)
        myll.insert(temp)
    print(f'#{tc} {myll.result()}')