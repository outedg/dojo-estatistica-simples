class EstatisticaSimples:

    def calcular_media(self, valores) -> float:
        return sum(valores) / len(valores)

    def calcular_valor_minimo(self, valores) -> float:
        if len(valores) > 0:
            return min(valores)
        return 0
