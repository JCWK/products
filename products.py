products = []
while True:
	name = input("Please input product name: ")
	if name == "q":
		break
	price = input("Please input product price: ")
	products.append([name, price])
print(products)

for p in products:
	print("The price of", p[0], "is HK$", p[1])