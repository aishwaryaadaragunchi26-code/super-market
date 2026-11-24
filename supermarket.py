customer = input("Enter cashier/customer name: ")
phone = input("Enter phone number: ")
bill_no = input("Enter bill number: ")
bill_date = input("Enter bill date: ")

p1 = input("Enter product 1 name: ")
q1 = int(input("Enter product 1 quantity: "))
price1 = float(input("Enter product 1 price: "))

p2 = input("Enter product 2 name: ")
q2 = int(input("Enter product 2 quantity: "))
price2 = float(input("Enter product 2 price: "))

subtotal1 = q1 * price1
subtotal2 = q2 * price2
total = subtotal1 + subtotal2