x = input("Enter value: ")
try:
    x = int(x, 0)
    print("Integer")
except:
    try:
        x = float(x)
        print("Float")
    except:
        if x.lower() == "true" or x.lower() == "false":
            print("Boolean")
        elif x.startswith("[") and x.endswith("]"):
            print("List")
        elif x.startswith("(") and x.endswith(")"):
            print("Tuple")
        elif x.replace(" ", "") == "{}":
            print("Dictionary")
        elif x.startswith("{") and x.endswith("}"):
            if ":" in x:
                print("Dictionary")
            else:
                print("Set")
        elif x.lower() == "none":
            print("NoneType")
        else:
            print("String")
