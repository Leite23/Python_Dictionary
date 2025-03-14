# Escreva uma função que recebe uma lista de compras e um dicionario contendo o preço de cada produto disponivel em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponiveis nesta loja. Por exemplo, para os dados:

# lista_de_compras = ["banana", "maca", "laranja", "pera"]
# supermercado = {"amaciante":5,00, "banana":2,0, "maca":1,0, "laranja":3,00, "pera":5,00}
# o valor retornado pela funçao sera 16,00


def mercado(lista_de_compras, supermercado):
    total = 0
    for item in lista_de_compras:
        if item in supermercado:
            total += supermercado[item]
    return total


lista_de_compras = ["banana", "maca", "laranja", "pera"]
supermercado = {
    "amaciante": 5.00,
    "banana": 5.00,
    "maca": 1.00,
    "laranja": 3.00,
    "pera": 5.00,
}
print(mercado(lista_de_compras, supermercado))

