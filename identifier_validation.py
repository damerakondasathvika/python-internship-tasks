import keyword
x = input("Enter identifier: ")
if (x and
    (x[0].isalpha() or x[0] == "_") and
    x.replace("_","").isalnum() and
    not keyword.iskeyword(x)):
    print("Valid identifier")
else:
    print("Invalid identifier")