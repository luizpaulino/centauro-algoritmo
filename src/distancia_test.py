import unittest

from distancia import calcula_distancia_lojas, valida_dados_entrada, lojas_mais_proximas, ordenacao_insercao, tres_lojas_mais_proximas


class TestValidaDadosEntrada(unittest.TestCase):

    def setUp(self):
        self.posicao_cliente = [20, 101]
        self.plano = [100000, 100]

    def test_valida_dados_entrada_com_posicao_cliente_invalida(self):
        with self.assertRaises(Exception):

            resultado = valida_dados_entrada(
                plano=self.plano, posicao_cliente=self.posicao_cliente)

    def test_valida_dados_entrada_com_plano_invalido(self):
        with self.assertRaises(Exception):

            resultado = valida_dados_entrada(
                plano=plano, posicao_cliente=posicao_cliente)


class TestCalculaDistanciaLojas(unittest.TestCase):

    def setUp(self):
        self.lojas = [[40, 88], [99, 93], [
            99, 97], [18, 56], [99, 2], [99, 99]]
        self.posicao_cliente = [20, 32]
        self.distancias = calcula_distancia_lojas(
            posicao_cliente=self.posicao_cliente, lojas=self.lojas)
        self.lojas_proximas = [[18, 56], [40, 88], [99, 2]]
        self.plano = [100, 100]

    def test_calcula_distancia_lojas(self):

        resultado_esperado = {59.464274989274024: [40, 88], 99.80981915623332: [99, 93], 102.30347012687302: [
            99, 97], 24.08318915758459: [18, 56], 84.50443775329198: [99, 2], 103.58571330062848: [99, 99]}

        resultado = calcula_distancia_lojas(
            lojas=self.lojas, posicao_cliente=self.posicao_cliente)

        self.assertEqual(resultado, resultado_esperado)

    def test_ordenacao_insercao(self):
        lista_desordenada = [73, 20, 19, 3, 99, 5, 1]

        resultado_esperado = [1, 3, 5, 19, 20, 73, 99]

        resultado = ordenacao_insercao(lista_desordenada)

        self.assertEqual(resultado, resultado_esperado)

    def test_tres_lojas_mais_proximas(self):

        resultado = tres_lojas_mais_proximas(self.distancias)

        self.assertEqual(resultado, self.lojas_proximas)

    def test_lojas_mais_proximas(self):
        resultado = lojas_mais_proximas(
            self.posicao_cliente, self.lojas, self.plano)

        self.assertEqual(resultado, self.lojas_proximas)


if __name__ == '__main__':
    unittest.main()
