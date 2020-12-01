import unittest

from distancia import calcula_distancia_lojas

class TestLojaMaisProxima(unittest.TestCase):

    def test_lojas_mais_proximas_com_quatro_lojas(self):
        
        posicao_cliente = [20, 32]
        lojas = [[40, 88], [18, 56], [99, 2], [99,99]]
        plano = [100, 100]

        resultado = calcula_distancia_lojas(posicao_cliente, lojas, plano)

        self.assertEqual([[18, 56], [40, 88], [99, 2]], resultado)

    def test_lojas_mais_proximas_com_uma_loja(self):
        
        posicao_cliente = [20, 32]
        lojas = [[40, 88]]
        plano = [100, 100]

        resultado = calcula_distancia_lojas(posicao_cliente, lojas, plano)

        self.assertEqual([[40, 88]], resultado)

    def test_lojas_mais_proximas_com_posicao_cliente_invalida(self):
        with self.assertRaises(Exception):
            posicao_cliente = [20, 101]
            lojas = [[40, 88]]
            plano = [100, 100]

            resultado = calcula_distancia_lojas(posicao_cliente, lojas, plano)

if __name__ == '__main__':
    unittest.main()