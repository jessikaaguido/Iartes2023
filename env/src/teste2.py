def run_tests():
    estoque = TestEstoque()
    
    # Teste de venda bem-sucedida
    print(estoque.vender_medicamento('buprofeno', 5))  # Deve mostrar a mensagem de venda bem-sucedida
    
    # Teste de venda sem estoque suficiente
    print(estoque.vender_medicamento('dipirona', 20))  # Deve mostrar a mensagem de estoque insuficiente
    
    # Teste de venda de um medicamento não disponível
    print(estoque.vender_medicamento('paracetamol', 3))  # Deve mostrar a mensagem de medicamento não disponível
    
    # Teste de verificação de estoque
    print(estoque.verificar_estoque('Dorflex'))  # Deve mostrar a quantidade de estoque do Dorflex
    
    # Teste de verificação de estoque de medicamento não disponível
    print(estoque.verificar_estoque('ibuprofeno'))  # Deve mostrar a mensagem de medicamento não disponível
    
    # Teste de compra de medicamento
    print(estoque.comprar_medicamento('dipirona', 10))  # Deve mostrar a mensagem de compra bem-sucedida
    
    # Teste de compra de medicamento não disponível
    print(estoque.comprar_medicamento('paracetamol', 5))  # Deve mostrar a mensagem de medicamento não disponível
    
    # Teste de adição ao estoque
    print(estoque.comprar_medicamento('buprofeno', 15))  # Deve mostrar a mensagem de compra bem-sucedida e novo estoque
    
run_tests()
