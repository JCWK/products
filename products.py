import os

products = []
if os.path.isfile("products.csv"):
	print("File is found!")
	with open("products.csv", "r", encoding = "utf-8") as f:
		for line in f:
			if "Product name,Product price" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
	print(products)
else:
	print("File does not exist!")

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