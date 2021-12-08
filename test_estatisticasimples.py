from estatisticasimples import EstatisticaSimples
import pytest

@pytest.fixture
def setup():
    estatistica = EstatisticaSimples()
    valorMinimoEsperado = 10
    mediaEsperada = 15
    valorMaximoEsperado = 20
    lista = [10, 15, 20]
    return estatistica, valorMinimoEsperado, mediaEsperada, valorMaximoEsperado, lista

class TesteEstatisticaSimples:
    
    def test_deve_calcula_media(self, estatistica, media = setup):
        assert estatistica.calcular_media([10, 15, 20]) == media

    def test_deve_calcular_valor_minimo_de_uma_sequencia_numerica(self, estatistica, valorMinimoEsperado, lista = setup):
        valorRetornado = estatistica.calcular_valor_minimo(lista)
        assert valorRetornado == valorMinimoEsperado

    def test_nao_deve_explodir_se_a_lista_for_vazia(self, estatistica = setup):
        try:
            estatistica.calcular_valor_minimo([10])
        except ValueError:
            pytest.fail("Error")
    
    def test_deve_calcular_media(self, estatistica, mediaEsperada, lista = setup):
        assert mediaEsperada == estatistica.calcular_media(lista)

