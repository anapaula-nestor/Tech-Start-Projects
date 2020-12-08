import Category


class Product:
    __code: int
    __name: str
    __description: str
    __value: float
    __categories: list = []
    __weight: float
    __height: float
    __width: float
    __length: float

    def get_code(self) -> str:
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_description(self, desc):
        self.__description = desc

    def get_description(self) -> str:
        return self.__description

    def set_value(self, value):
        self.__value = value

    def get_value(self) -> str:
        return self.__value

    def set_categories(self, code):
        self.__categories.append(code)

    def get_categories(self):
        return self.__categories

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_heigh(self, heigh):
        self.__heigh = heigh

    def get_heigh(self):
        return self.__heigh

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length


def insertProduct(cat, product) -> Product:
    print("Please fill the information bellow:\n")

    prod = Product()

    j = False
    # lenProducts = len(products)
    while not j:
        j = True
        code = input("Product code: ")
        name = input("Product name: ")
        value = input("Product Price: ")
        description = input("Product description: ")
        weight = input("Product weight: ")
        heigh = input("Product heigh: ")
        width = input("Product width: ")
        length = input("Product length: ")

        validate = searchProduct(code, product)

        if validate is None:
            j = validateFloat(value)
            j = validateFloat(weight)
            j = validateFloat(heigh)
            j = validateFloat(width)
            j = validateFloat(length)
            j = True if len(description) >= 20 else False
        else:
            j = False

        if j:
            prod.set_code(code)
            prod.set_name(name)
            prod.set_value(value)
            prod.set_description(description)
            prod.set_weight(weight)
            prod.set_heigh(heigh)
            prod.set_width(width)
            prod.set_length(length)

            Category.readCategories(cat)
            print("Please type the category code for the product based on the list above:\n")
            answer = "y"
            while answer == "y":
                code = input("Code: ")
                prod.set_categories(code)
                print("Would like to enter another category? Type y(yes) or n(no).")
                answer = input("Answer: ")

        else:
            print("Some information has a mistake or you are trying to use a code already registered. Please try "
                  "again.\n")

    # category = input("Category name: ")
    # criar e chamar metodo para inserir cateria
    # products.append([code, name, category, value])
    print("Product inserted successfully.")
    return prod


def updateProduct(product):
    code = input("Please type the product code: ")
    prod = searchProduct(code, product)
    j = False
    # lenProducts = len(products)
    while not j:
        j = True
        # code = input("Product code: ")
        # code = code if code != "" else prod.get_code()
        name = input("Product name: ")
        name = name if name != "" else prod.get_name()
        value = input("Product Price: ")
        value = value if value != "" else prod.get_value()
        description = input("Product description: ")
        description = description if description != "" else prod.get_description()
        weight = input("Product weight: ")
        weight = weight if weight != "" else prod.get_weight()
        heigh = input("Product heigh: ")
        heigh = heigh if heigh != "" else prod.get_heigh()
        width = input("Product width: ")
        width = width if width != "" else prod.get_width()
        length = input("Product length: ")
        length = length if length != "" else prod.get_length()

        j = validateFloat(value)
        j = validateFloat(weight)
        j = validateFloat(heigh)
        j = validateFloat(width)
        j = validateFloat(length)
        j = True if len(description) >= 20 else False

        if j:
            # prod.set_code(code)
            prod.set_name(name)
            prod.set_value(value)
            prod.set_description(description)
            prod.set_weight(weight)
            prod.set_heigh(heigh)
            prod.set_width(width)
            prod.set_length(length)
        else:
            print(
                "Some information a has mistake. Please try again.\n")


def deleteProduct(prod):
    code = input("Please type the product code: ")
    p = searchProduct(code, prod)

    if p is None:
        print("Product not found.")
    else:
        prod.remove(p)
        print("Product removed successfully.")


def readProduct(prod, cat):
    code = input("Please type the product code: ")
    p = searchProduct(code, prod)

    if p is None:
        print("Product not found.")
    else:
        print("Code: " + p.get_code())
        print("Name: " + p.get_name())
        print("Value: " + p.get_value())
        print("description: " + p.get_description())
        print("Weight: " + p.get_weight())
        print("Heigh: " + p.get_heigh())
        print("Width: " + p.get_width())
        print("Length: " + p.get_length())
        print("Categories: ")
        for i in p.get_categories():
            Category.readCategory(i, cat)


def searchProduct(code, prod):
    for i in prod:
        if code == i.get_code():
            return i


def validateFloat(number):
    try:
        if float(number) > 0:
            return True
        else:
            print("Please, type a value bigger than 0.")
            return False
    except ValueError as error:
        print("Please, type a valid number.")
