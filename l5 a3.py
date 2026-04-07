product_amount = float(input("Pleas enter your product price : "))
sale_amount = float(input("Please enter your sales amount : "))

if sale_amount > product_amount :
    amount = sale_amount - product_amount
    print("Total Profit : ", amount)
else :
    ("No profit !!!")