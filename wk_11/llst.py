
class Node:

    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3

    current = n1
    while current is not None:
        print(current.val)
        current = current.next
    print(current)