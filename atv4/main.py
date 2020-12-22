marketplace = ['Submarino', 'Americanas', 'Shoptime', 'Mercado Livre']
categories = ['eletrônicos', 'móveis', 'quarto', 'Beleza', 'Produtos de Limpeza']
subcategories = [['Celulares', categories[0]], ['cama', categories[2]], ['mesa', categories[1]],
                 ['Veja', categories[4]],['Batom',categories[3]]]


def read_marketplaces():
    return marketplace


def read_categories():
    return categories


def read_subcategories(category):
    sub = []
    for i in subcategories:
        if i[1] == category:
            sub.append(i[0])
    return sub


# print(read_subcategories('eletrônicos'))
