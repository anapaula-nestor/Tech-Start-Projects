# path = 'Data/'

path = 'Data/historic.txt'


def read_historic() -> list:
    result = []
    file = open(path, 'r')
    for line in file:
        new_line = line.strip().split(';')
        result.append(new_line)
    file.close()
    return result


def read_column(column_name) -> list:
    result = []
    file = open(path, 'r')
    position = 0
    column = None
    for line in file:
        new_line = line.strip().split(';')
        if position == 0:
            for name in new_line:
                if column_name == name:
                    column = new_line.index(name)
                    position = 1
        else:
            if new_line[column] not in result:
                result.append(new_line[column])
    file.close()
    return result


def read_categories(marketplace_name) -> list:
    result = []
    full_list = read_historic()
    for item in full_list:
        if item[0] == marketplace_name:
            if item[1] not in result:
                result.append(item[1])
    return result


def read_subcategories(marketplace_name, category_name) -> list:
    result = []
    full_list = read_historic()
    for item in full_list:
        if item[1] == category_name and item[0] == marketplace_name:
            if item[2] not in result:
                result.append(item[2])
    return result


# teste = read_historic()
# for i in teste:
#    print(i)

#print(read_subcategories("Americanas", "Móveis"))
