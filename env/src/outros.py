class FarmaciaVarejo (object):
    def __init__(self): 
        self._estoque_ = {'buprofeno': 10, 'dipirona': 15, 'Dorflex':5 }
        
    def adicionar_produto(self, produto, quantidade):
        if produto in self._estoque_:
            self._estoque_[produto] += quantidade
        else:
            self._estoque_[produto] = quantidade
            
    def vender_produto(self, produto, quantidade):
        if produto in self._estoque_ and self._estoque_[produto] >= quantidade:
            self._estoque_[produto] -= quantidade
            return f"{quantidade} unidades de {produto} vendidas."
        elif produto in self._estoque_:
            return f"Estoque insuficiente de {produto}."
        else:
            return f"{produto} não está disponível no estoque."
    
    def verificar_estoque(self, produto):
        if produto in self._estoque_:
            return f"No estoque, há {self._estoque_[produto]} unidades de {produto}."
        else:
            return f"{produto} não está disponível no estoque."






