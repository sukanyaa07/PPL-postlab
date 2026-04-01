from block import Block

class MemoryAllocator:
    def __init__(self, total_size):
        self.head = Block(0, total_size, True)

    def display(self):
        temp = self.head
        print("\nMemory Status:")
        print("Start\tSize\tStatus")
        while temp:
            status = "Free" if temp.free else "Allocated"
            print(f"{temp.start}\t{temp.size}\t{status}")
            temp = temp.next

    def allocate(self, size):
        temp = self.head
        while temp:
            if temp.free and temp.size >= size:
                if temp.size == size:
                    temp.free = False
                else:
                    new_block = Block(temp.start + size, temp.size - size, True)
                    new_block.next = temp.next
                    temp.size = size
                    temp.free = False
                    temp.next = new_block

                print(f"\nAllocated {size} units at address {temp.start}")
                return
            temp = temp.next

        print("\nMemory Allocation Failed!")

    def deallocate(self, start_address):
        temp = self.head
        while temp:
            if temp.start == start_address and not temp.free:
                temp.free = True
                print(f"\nDeallocated block at address {start_address}")
                self.merge()
                return
            temp = temp.next

        print("\nInvalid Address or Already Free!")

    def merge(self):
        temp = self.head
        while temp and temp.next:
            if temp.free and temp.next.free:
                temp.size += temp.next.size
                temp.next = temp.next.next
            else:
                temp = temp.next