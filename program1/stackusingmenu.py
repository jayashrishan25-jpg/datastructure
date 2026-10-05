stack = []

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        stack.append(x)
        print("Pushed")

    elif choice == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack Underflow")

    elif choice == 3:
        if stack:
            print("Top:", stack[-1])
        else:
            print("Stack Empty")

    elif choice == 4:
        print("Stack:", stack)

    elif choice == 5:
        break

    else:
        print("Invalid choice")