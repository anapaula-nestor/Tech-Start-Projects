class Category:
    __code: int
    __name: str
    __mainCategoryCode: int

    def get_code(self) -> str:
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_mainCategoryCode(self, code):
        self.__mainCategoryCode = code

    def get_mainCategoryCode(self):
        return self.__mainCategoryCode


def insertCategory():
    cat = Category()
    print("Please fill the information bellow:\n")
    cat.set_code(input("Code category: "))
    cat.set_name(input("Name category: "))

    print(cat.get_code() + " " + cat.get_name())
    answer = input("Is this a subcategory? Please answer y for yes or n for no: ")
    if answer == "y":
        # readCategories(category)
        cat.set_mainCategoryCode(input("Code main category: "))
    return cat


def readCategories(category):
    print("Categories already registered:")
    for i in category:
        print("Code: " + i.get_code() + "\nName:" + i.get_name() + "\n\n")


def readCategory(code, cat):
    for i in cat:
        if code == i.get_code():
            print(i.get_code() + "-" + i.get_name())
