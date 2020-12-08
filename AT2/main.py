import Product
import Category

prodList = []
catList = []


def getAction() -> int:
    print(
        "\n1 - Create product\n2 - Update product\n3 - Delete product\n4 - Read products\n5 - Add Category\n6 - exit\n")
    value = 0
    while value == 0:
        value = input("Please choose one option: ")
        if value == "" or value.isdigit() is False or value == 0:
            print("The option must be a number in the list. Please try again.")
            value = 0
    return int(value)


choice = 0
print(catList)
while choice != 6:
    choice = getAction()
    if choice == 1:
        if len(catList) == 0:
            print("Please register at least one category before insert a product.")
            continue
        prodList.append(Product.insertProduct(catList, prodList))
    elif choice == 2:
        Product.updateProduct(prodList)
    elif choice == 3:
        Product.deleteProduct(prodList)
    elif choice == 4:
        Product.readProduct(prodList, catList)
    elif choice == 5:
        Category.readCategories(catList)
        catList.append(Category.insertCategory())

exit()
