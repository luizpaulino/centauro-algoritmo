import math


def valida_dados_entrada(plano: list[int], posicao_cliente: list[int]):
    if (plano[0] < 0) or (plano[0] > 1000):
        raise Exception('Plano M inválido')

    if (plano[1] < 0) or (plano[1] > 1000):
        raise Exception('Plano N inválido')

    cliente_x = posicao_cliente[0]
    cliente_y = posicao_cliente[1]

    if (cliente_x < 0) or (cliente_x > plano[0]):
        raise Exception('Posição X do cliente inválida')

    if (cliente_y < 0) or (cliente_y > plano[1]):
        raise Exception('Posição Y do cliente inválida')


def calcula_distancia_lojas(posicao_cliente: list[int], lojas: list[list[int]]):
    distancias = {}

    cliente_x = posicao_cliente[0]
    cliente_y = posicao_cliente[1]

    for loja in lojas:

        loja_x = loja[0]
        loja_y = loja[1]

        distancia = ((loja_x - cliente_x) ** 2) + ((loja_y - cliente_y) ** 2)
        distancia_ab = math.sqrt(distancia)

        distancias.update({
            distancia_ab: loja
        })

    return distancias


def ordenacao_insercao(distancias: list[int]):
    for i in range(1, len(distancias)):

        distancia_atual = distancias[i]
        j = i-1
        while j >= 0 and distancia_atual < distancias[j]:
            distancias[j+1] = distancias[j]
            j -= 1
        distancias[j+1] = distancia_atual

    return distancias


def tres_lojas_mais_proximas(todas_lojas: dict):
    distancia_todas_lojas = list(todas_lojas.keys())

    lojas_ordenadas = ordenacao_insercao(distancia_todas_lojas)
    tres_lojas_mais_proximas = []

    for loja in lojas_ordenadas[0:3]:
        tres_lojas_mais_proximas.append(todas_lojas[loja])

    return tres_lojas_mais_proximas


def lojas_mais_proximas(posicao_cliente: list[int], lojas: list[list[int]], plano: list[int]):

    valida_dados_entrada(plano=plano, posicao_cliente=posicao_cliente)

    distancias = calcula_distancia_lojas(
        posicao_cliente=posicao_cliente, lojas=lojas)

    lojas = tres_lojas_mais_proximas(distancias)

    return lojas


if __name__ == "__main__":
    posicao_cliente = [20, 32]
    lojas = [[40, 88], [99, 93], [99, 97], [18, 56], [99, 2], [99, 99]]
    plano = [100, 100]

    resultado = lojas_mais_proximas(posicao_cliente, lojas, plano)

    print(resultado)
