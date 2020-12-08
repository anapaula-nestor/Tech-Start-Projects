class Product:
    __code: int
    __name: str
    __description: str
    __value: float
    __subcategories: list()
    __weight: float
    __height: float
    __width: float
    __length: float

    def get_code(self) -> str:
        return self.__code

    def set_name(self, code):
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

    def set_subcategories(self, subcategories):
        self.__subcategories = subcategories

    def get_subcategories(self):
        return self.__subcategories

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


def insertProduct() -> Product:
    print("Please fill the information bellow:\n")
    #code = 0
    prod = Product()
    code = input("Product code: ")
    # lenProducts = len(products)

    prod.set_code(code)
    prod.set_name(input("Product name: "))
    prod.set_value(input("Product Price: "))
    # category = input("Category name: ")
    # criar e chamar metodo para inserir cateria
    # products.append([code, name, category, value])
    print("Product inserted successfully.")
    return prod


def updateProduct():
    code = input("Please type the product code: ")


#    lenProducts = len(products)
#    for i in range(0, lenProducts):
#        if code == products[i][0]:
#            name = input("Please type the new product name: ")
#            category = input("Please type the new category name: ")
#            value = input("Please type the new price: ")

#            products[i][1] = name if name != "" else products[i][1]
#            products[i][2] = category if category != "" else products[i][2]
#            products[i][3] = value if value != "" else products[i][3]


def deleteProduct():
    code = input("Please type the product code: ")


#    lenProducts = len(products)
#    for i in range(0, lenProducts):
#        if code == products[i][0]:
#            del products[i]


def readProduct(prod):
    for i in prod:
        print(i)
