class TestEstoque(object):
    def __init__(self): 
        self._estoque_produto = ('buprofeno', 10, 'dipirona', 15, 'Dorflex', 5)
        
    def vender_medicamento(self, medicamento, quantidade):
        if medicamento in self._estoque_produto:
            index = self._estoque_produto.index(medicamento)
            estoque_atual = self._estoque_produto[index + 1]
            if quantidade <= estoque_atual:
                novo_estoque = estoque_atual - quantidade
                self._estoque_produto = list(self._estoque_produto)
                self._estoque_produto[index + 1] = novo_estoque
                self._estoque_produto = tuple(self._estoque_produto)
                return f"{quantidade} unidades de {medicamento} vendidas."
            else:
                return f"Não há estoque suficiente de {medicamento}."
        else:
            return f"{medicamento} não está disponível no estoque."
            
    def verificar_estoque(self, medicamento):
        if medicamento in self._estoque_produto:
            index = self._estoque_produto.index(medicamento)
            estoque_atual = self._estoque_produto[index + 1]
            return f"No estoque, há {estoque_atual} unidades de {medicamento}."
        else:
            return f"{medicamento} não está disponível no estoque."
    
    def comprar_medicamento(self, medicamento, quantidade):
        if medicamento in self._estoque_produto:
            index = self._estoque_produto.index(medicamento)
            estoque_atual = self._estoque_produto[index + 1]
            novo_estoque = estoque_atual + quantidade
            self._estoque_produto = list(self._estoque_produto)
            self._estoque_produto[index + 1] = novo_estoque
            self._estoque_produto = tuple(self._estoque_produto)
            return f"Adquiridas {quantidade} novas unidades de {medicamento}. Novo estoque: {novo_estoque}."
        else:
            return f"{medicamento} não está disponível para compra."
