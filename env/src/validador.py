class Validador (object):
    def __init__(self): 
        self._cod_area = (11, 12, 19, 65, 68, 92, 93)  
        
    def ano_bissexto(self,ano):
        pass
        
    def validar_data(self, data):
        pass
        
    def validar_telefone (self, telefone):
        telefone_valido = True
        if len(telefone) != 13:
            telefone_valido = False
        # elif len(telefone[4:]) != 9:
        #     telefone_valido = False
        elif telefone[0] != '(' or telefone[3] != ')':
            telefone_valido = False        
        if int(telefone[1:3]) not in self._cod_area:
            telefone_valido = False

        return telefone_valido
