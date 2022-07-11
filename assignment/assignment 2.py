amount=int(input("Enter the quantity: "))
discount= amount*0.1
if amount>1000:
  price=amount-discount
  print(price)
else:
  price=amount
  print(price)
