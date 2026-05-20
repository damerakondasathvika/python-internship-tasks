password=input("enter password:")
if ("@" in password or "#" in password or "$" in password)and(" " not in password):
    print("Strong password")
else:
    print("Weak password")