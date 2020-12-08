class Category:
    __code: int
    __name: str
    __subcategories: list()

    def get_code(self) -> str:
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_subcategories(self, code, subcategory):
        self.__subcategories.append([code, subcategory])

    def get_subcategories(self):
        return self.__subcategories


def insertCategory():
    cat = Category()
    cat.set_code(input("Code: "))
    cat.set_name(input("Name: "))
    subCode = input("Code subcategory: ")
    subName = input("Name subcategory: ")
    cat.set_subcategories(subCode, subName)

    print(cat.get_subcategories())


insertCategory()


