percentage =int(input("enter percentage:"))
income =int(input("enter family income:"))
eligible = percentage >85 or (percentage >75 and income < 200000)
print("Eligible for merit scholarship:",eligible)
#output
#enter percentage:86
#enter family income:300000
#Eligible for merit scholarship: True
