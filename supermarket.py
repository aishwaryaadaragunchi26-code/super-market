import sys

customer = sys.argv[1]
phone = sys.argv[2]
bill_no = sys.argv[3]
bill_date = sys.argv[4]

p1 = sys.argv[5]
q1 = int(sys.argv[6])
price1 = float(sys.argv[7])

p2 = sys.argv[8]
q2 = int(sys.argv[9])
price2 = float(sys.argv[10])

subtotal1 = q1 * price1
subtotal2 = q2 * price2
total = subtotal1 + subtotal2

print("\n--------- SHOPPING BILL ---------")
print("Cashier/Customer Name:", customer)
print("Phone Number:", phone)
print("Bill Number:", bill_no)
print("Bill Date:", bill_date)

print("\nProduct 1:", p1)
print("Quantity:", q1)
print("Price:", price1)
print("Subtotal 1:", subtotal1)

print("\nProduct 2:", p2)
print("Quantity:", q2)
print("Price:", price2)
print("Subtotal 2:", subtotal2)

print("\nTotal Amount:", total)
print("--------------------------------")