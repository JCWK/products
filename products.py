import os

def read_file(filename):
    products = []
    with open(filename, "r", encoding = "utf-8") as f:
        for line in f:
            if "Product name,Product price" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    print(products)
    return products

def user_input(products):
    while True:
        name = input("Please input product name: ")
        if name == "q":
            break
        price = input("Please input product price: ")
        price = float(price)
        products.append([name, price])
    print(products)
    return products

def print_products(filename, products):
    print("The file(", filename, ") is created. Below are the data you just added. \n")
    print("Product name", "    ", "Product price")
    for p in products:
        print(p[0], "    ", p[1])

def write_file(filename, products):
    with open (filename, "w") as f:
        f.write("Product name" + "," + "Product price" + "\n")
        for p in products:
            f.write(p[0] + "," + str(p[1]) + "\n")

def main():
    filename = "products.csv"
    if os.path.isfile(filename):
        print("File is found!")
        products = read_file(filename)
    else:
        print("File does not exist!")
    products = user_input(products)
    print_products(filename, products)
    write_file(filename, products)

main()