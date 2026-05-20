x = input("Enter value: ")
try:
    x = int(x)
    print("Integer")
except:
    try:
        x = float(x)
        print("Float")
    except:
        if x == "True" or x == "False":
            print("Boolean")
        else:
            print("String")