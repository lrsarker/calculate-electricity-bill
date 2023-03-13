# Electricity Bill

c_id = int(input("Enter your ID Number: "))
c_name = input("Enter your User Name: ")
c_unit = float((input("Enter your Unit Consumed: ")))

#calculate rate
rate = None

if c_unit >=600:
    rate = 2.0
elif c_unit >=400:
    rate = 1.80

elif c_unit >=200:
    rate = 1.50
else:
    rate = 1.20

#Calculate Bill

bill = rate * c_unit

#check minimum bill amount
if bill <100:
    bill=100

# Calculate surcharge
surcharge = 0

if bill > 400:
    surcharge = bill * 15 * 1/100
net_bill = surcharge + bill

print("Customer ID NO:", c_id)
print("Customer Name:", c_name)
print("Unit Consumed:", c_unit)
print("Amount Charges @TK:", rate, "per unit:", bill)
print("Surcharge Amount: ", surcharge)
print("Net Amount Paid By the Customer:", net_bill)
