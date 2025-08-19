# Problema 4 – Stivă (20p)

class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        # TODO
        pass

    def pop(self):
        # TODO
        pass

    def peek(self):
        # TODO
        pass

    def __repr__(self):
        return f"Stack({self._data})"

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(7)
    s.pop()
    s.push(9)
    print(s.peek())  # 9
    print(s)
