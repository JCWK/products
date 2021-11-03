products = []
while True:
	name = input("Please input product name: ")
	if name == "q":
		break
	price = input("Please input product price: ")
	price = float(price)
	products.append([name, price])
# print(products)

print("The file(products.csv) is created. Below are the data you just added. \n")
print("Product name", "    ", "Product price")
for p in products:
    print(p[0], "    ", p[1])

with open ("products.csv", "w") as f:
	f.write("Product name" + "," + "Product price" + "\n")
	for p in products:
		f.write(p[0] + "," + str(p[1]) + "\n")