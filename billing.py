total = 0
item_count = 0
while True:
    product = input("Product name: ")
    if product == "":
        break
    cost = float(input("Price:"))
    quantity = int(input("Quantity: "))
    bill = cost * quantity
    total = total + bill
    item_count = item_count + 1
    print(product, "x", quantity, "=", bill)
if total >= 5000:
    discount = total * 0.20
    discount_percent = 20
elif total >= 2000:
    discount = total * 0.15
    discount_percent = 15
elif total >= 1000:
    discount = total * 0.10
    discount_percent = 10
else:
    discount = 0
    discount_percent = 0
final_bill = total - discount
print("RECEIPT")
print("Items purchased:", item_count)
print("Total Amount:", total)
print("Discount:", discount_percent, "%")
print("Discount Amount:", discount)
print("Final Amount:", final_bill)
print("THANK YOU")