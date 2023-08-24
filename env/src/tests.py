class TestTelefone (object):
    def test_format_cod_area_invalido(self):
        v = val.Validador()
        assert v.validar_telefone('(00)99984567') == False
        
    def test_tam_invalido(self):
        v = val.Validador()
        assert v.validar_telefone('[92]999984567') == False
        
    def test_ddd_invalido(self):
        v = val.Validador()
        telefone = '(92)999664444'
        assert v.validar_telefone(telefone) == False
    
    def test_cod_area_invalido(self):
        v = val.Validador()
        assert v.validar_telefone('(45)999984567') == False
        
    def test_format_cod_area_invalido(self):
        v = val.Validador()
        assert v.validar_telefone('(4)999984567') == False
    