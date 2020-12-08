import Product


def insertProd() -> Product:
    prod = Product()
    prod.set_name(input("Name: "))
    prod.set_value(input("insira o valor: "))
    return prod


prodList = []

prodList.append(Product.insertProduct())

for i in prodList:
    print(i)
    print(i.get_name())


def getAction() -> int:
    print("\n1 - Create product\n2 - Update product\n3 - Delete product\n4 - Read products\n5 - exit\n")
    value = 0
    while value == 0:
        value = input("Please choose one option: ")
        if value == "" or value.isdigit() is False or value == 0:
            print("The option must be a number in the list. Please try again.")
            value = 0
    return int(value)

choice = 0

while choice != 5:
    choice = getAction()
    if choice == 1:
        prodList.append(Product.insertProduct(prodList))
    elif choice == 2:
        Product.updateProduct()
    elif choice == 3:
        Product.deleteProduct()
    elif choice == 4:
        Product.readProduct()

exit()
