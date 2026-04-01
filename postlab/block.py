class Block:
    def __init__(self, start, size, free=True):
        self.start = start
        self.size = size
        self.free = free
        self.next = None