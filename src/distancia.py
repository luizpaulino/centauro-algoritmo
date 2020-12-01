import math

def calcula_distancia_lojas(posicao_cliente: list[int], lojas: list[list[int]], plano: list[int]):
  distancias = {}

  for loja in lojas:

    if (plano[0] < 0) or (plano[0] > 1000):
      raise Exception('Plano M inválido')

    if (plano[1] < 0) or (plano[1] > 1000):
      raise Exception('Plano N inválido')


    loja_x = loja[0]
    loja_y = loja[1]

    cliente_x = posicao_cliente[0]
    cliente_y = posicao_cliente[1]

    if (cliente_x < 0) or (cliente_x > plano[0]):
      raise Exception('Posição X do cliente inválida')
    
    if (cliente_y < 0) or (cliente_y > plano[1]):
      raise Exception('Posição Y do cliente inválida')

    distancia = ((loja_x - cliente_x) ** 2) + ((loja_y - cliente_y) ** 2) 
    distancia_ab = math.sqrt(distancia)

    distancias.update({
      distancia_ab: loja
    })

  todas_lojas = list(distancias.keys())
  todas_lojas.sort()
  todas_lojas = todas_lojas[0:3]

  lojas_mais_proximas = []

  for loja in todas_lojas:
    lojas_mais_proximas.append(distancias[loja])

  return lojas_mais_proximas

