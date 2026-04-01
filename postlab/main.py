from memory_allocator import MemoryAllocator

def main():
    try:
        total_memory = int(input("Enter total memory size: "))
    except ValueError:
        print("Invalid input!")
        return

    allocator = MemoryAllocator(total_memory)

    while True:
        print("\n1. Allocate")
        print("2. Deallocate")
        print("3. Display Memory")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Enter valid number!")
            continue

        if choice == 1:
            try:
                size = int(input("Enter block size: "))
                allocator.allocate(size)
            except ValueError:
                print("Invalid size!")

        elif choice == 2:
            try:
                addr = int(input("Enter starting address: "))
                allocator.deallocate(addr)
            except ValueError:
                print("Invalid address!")

        elif choice == 3:
            allocator.display()

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()