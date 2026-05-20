total=0
n=int(input("enter number of products:"))
for i in range(n):
    product=input("enter product name:")
    cost=int(input("enter cost of product:"))
    quantity=int(input("enter number of quantity:"))
    bill=cost*quantity
    total=bill+total
print("Total bill:",total)
