def is_between(number1, number2, number3):
    if number2 >= number1:
        if number2 <= number3:
            return True
    elif number2 >= number3:
        if number1 <= number1:
            return True
    return False


def dot(a, b):
    return sum([a[i] * b[i] for i in range(len(b))])


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0: return 0  # Collinear
    if val > 0: return 1  # Clockwise
    return 2  # Anti clockwise


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        self.intersection = None

    def __repr__(self):
        return repr(self.data)

    def __eq__(self, other):
        if self.data == other.data:
            return True
        return False


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def prepend(self, data):
        self.head = Node(data=data, next=self.head)

    def insert(self, data, prev):
        if self.find(prev):
            prev = self.find(prev)
            node = Node(data=data, next=prev.next)
            prev.next = node

    def remove(self, data):
        curr = self.head
        prev = None
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def find(self, data):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        return curr

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def __getitem__(self, item):
        curr = self.head
        for i in range(item):
            curr = curr.next
        return curr

    def __setitem__(self, key, value):
        if key == 0:
            self.head = Node(data=value, next=self.head.next)
            return
        prev = self.head
        for i in range(key - 1):
            prev = prev.next
        prev.next = Node(data=value, next=prev.next.next)

    def to_array(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.data)
            curr = curr.next
        return nodes
