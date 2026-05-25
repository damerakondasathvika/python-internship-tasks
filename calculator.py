x = int(input("Enter first number: "), 0)
y = int(input("Enter second number: "), 0)
print("1. AND")
print("2. OR")
print("3. XOR")
print("4. NOT")
print("5. SHIFT")
choice = int(input("Enter operation: "))
if choice == 1:
    result = x & y
    print("Binary Result:", bin(result))
    print("Result:", result)
elif choice == 2:
    result = x | y
    print("Binary Result:", bin(result))
    print("Result:", result)
elif choice == 3:
    result = x ^ y
    print("Binary Result:", bin(result))
    print("Result:", result)
elif choice == 4:
    print("1. NOT x")
    print("2. NOT y")
    not_choice = int(input("Enter choice: "))
    if not_choice == 1:
        result = ~x
    elif not_choice == 2:
        result = ~y
    else:
        print("Invalid choice")
        exit()
    print("Binary Result:", bin(result))
    print("Result:", result)
elif choice == 5:
    print("1. Left Shift x")
    print("2. Right Shift x")
    print("3. Left Shift y")
    print("4. Right Shift y")
    shift = int(input("Enter shift choice: "))
    if shift == 1:
        result = x << 1
    elif shift == 2:
        result = x >> 1
    elif shift == 3:
        result = y << 1
    elif shift == 4:
        result = y >> 1
    else:
        print("Invalid shift")
        exit()
    print("Binary Result:", bin(result))
    print("Result:", result)
else:
    print("Invalid operation")