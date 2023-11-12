import math

Inicio = """

[1] -> Metano :
"O cálculo de Metano e Baseado em aterros sanitários obtendo informações de Habitantes do tamanho do Aterro e a quantidade de anos que ele será utilizado. Com isso realizamos 3 PERGUNTAS com 2 variaveis SIM e NÂO dependendo da Resposta você consiguirá produzir crédito de Carbono"

[2] -> Oxido Nitroso:
"O cálculo de Oxido Nitroso e baseado em carros de aplicativos utilizados em Cidades Inteligentes, com base no modelo do carro, no Trafego e com algumas perguntas baseadas na queima de combustivel conseguimos criar uma previsão da quantidade de crédito que pode ser acumulada em um determinado periodo.

[3] -> Dioxido de Carbono
"O cálculo de carbono e baseado em Árvores plantadas com mais de 20 anos para produzir crédito de carbono onde o usuario realiza somente a quantidade de Hectares onde está a árvore podendo repetir 3 vezes o cálculo"

[0] -> Sair

"""


while True: 
    print(">>>>>>>>>>SELECIONE UMA DAS OPÇÕES PARA CALCULAR<<<<<<<<")
    print(Inicio)
    select = int(input("Digite o número correspondente a opção: "))

    if select == 1:
        print("======================================================================================================================================================")
        print("""O cálculo de Metano e Baseado em aterros sanitários obtendo informações de Habitantes do tamanho do Aterro
e a quantidade de anos que ele será utilizado. Com isso realizamos 3 PERGUNTAS com 2 variaveis SIM e NÂO dependendo da Resposta você consiguirá produzir crédito de Carbono""")
        print("======================================================================================================================================================")

        while True:

            PERGUNTAS = """
            [1] -> Você pretende realizar captura de Metano ao decorrer do tempo em seu aterramento?
            
            [2] -> Você peretende realizar a Reciclagem de Residuos Orgânicos?

            [3] -> Você pretende utilizar tecnologia de Cobertura Aerossol?
            """

            Captura_Metano = 0.5
            Reciclagem = 0.7
            Cobertura = 0.2
            Credito_Acumu = 0

            Habitantes = float(input("Digite a quantidade de Habitantes da cidade: "))
            Aterro = float(input("Digite o tamanho do aterro cidade: "))
            Aterro_tempo = float(input("Digite quantos anos ficará o aterro: ")) 
            k = Aterro / (100 * Aterro_tempo) 
            k_1 = 0.02
            k_2 = 0.01
            media_dia = 1
            a = Reciclagem * Aterro_tempo
            print(a)
            Residuos_Depositados = Habitantes * media_dia * Aterro_tempo
            print(Residuos_Depositados)
            Taxa_Producao = k * Residuos_Depositados * (1 + k_1 * math.exp(-k_2 * Aterro_tempo))
            Taxa_BASELINE = k * Residuos_Depositados * (1 + k_1 * math.exp(-k_2 * Aterro_tempo))
            print(Taxa_Producao )
            cr_car = Taxa_BASELINE - Taxa_Producao


            resposta = False
            print(PERGUNTAS)
            P_1 = input('Responda Sim ou Não para a pergunta [1]: ').upper()
            if P_1 != 'SIM' and P_1 != 'NAO':
                print("DIGITE SIM OU NAO")
                continue
            elif P_1 == "SIM":
                resposta = True 
                Reduc = Captura_Metano * Aterro_tempo
                Taxa_Producao -= Reduc
                Credito_Acumu = Taxa_BASELINE - Taxa_Producao
                R = Credito_Acumu * 81.67
                print(f'Com essa ação você acumulou cerca de {Credito_Acumu:.2f}T seu saldo atualizado e de R$ {R:.2f} ')
                while True:
                    P_2 = input('Responda Sim ou Não para a pergunta [2]: ').upper()
                    if P_2 != "SIM" and P_2 != "NAO":
                        print("DIGITE SIM OU NAO")
                    elif P_2 == "SIM":
                        Reduc = Reciclagem * Aterro_tempo
                        Taxa_Producao -= Reduc
                        Credito_Acumu = Taxa_BASELINE - Taxa_Producao
                        R += Credito_Acumu * 81.67
                        print(f'Com essa ação você acumulou cerca de {Credito_Acumu:.2f}T seu saldo atualizado e de a R$ {R:.2f} ')
                        resposta = True
                        while True:
                            P_3 = input('Responda Sim ou Não para a pergunta [3]: ').upper()
                            if P_3 != "SIM" and P_3 != "NAO":
                                print("DIGITE SIM OU NAO")
                            elif P_3 == "SIM":
                                resposta = True
                                Reduc = Cobertura * Aterro_tempo
                                Taxa_Producao -= Reduc
                                Credito_Acumu = Taxa_BASELINE - Taxa_Producao
                                R += Credito_Acumu * 81.67
                                print(f'Com essa ação você acumulou cerca de {Credito_Acumu:.2f}T seu saldo atualizado e de R$ {R:.2f}')
                            elif P_3 == 'NAO':
                                resposta = True
                                print(f'>>>>>>>>>Você tem cerca de {Credito_Acumu:.2f}T credito acumulado seu saldo atualizado e de R$ {R:.2f}<<<<<<<<<<<<<<')
                            if resposta == True:
                                break    
                    elif P_2 == 'NAO':
                        resposta = True
                        print(f'>>>>>>>>>Você tem cerca de {Credito_Acumu:.2f}T credito acumulado seu saldo atualizado e de R$ {R:.2f}<<<<<<<<<<<<<<')   
                        while True:
                            P_3 = input('Responda Sim ou Não para a pergunta [3]: ').upper()
                            if P_3 != "SIM" and P_3 != "NAO":
                                print("DIGITE SIM OU NAO")
                            elif P_3 == "SIM":
                                resposta = True
                                Reduc = Cobertura * Aterro_tempo
                                Taxa_Producao -= Reduc
                                Credito_Acumu = Taxa_BASELINE - Taxa_Producao
                                R += Credito_Acumu * 81.67
                                print(f'Com essa ação você acumulou cerca de {Credito_Acumu:.2f}T seu saldo atualizado e de R$ {R:.2f}')
                            elif P_3 == 'NAO':
                                resposta == True
                                print(f'>>>>>>>>>Você tem cerca de {Credito_Acumu:.2f}T credito acumulado seu saldo atualizado e de R$ {R:.2f}<<<<<<<<<<<<<<')
                            if resposta == True:
                                break
                    if resposta == True:
                        break 
            elif P_1 == "NAO":
                resposta: True
                print(f'>>>>>>>>>Você tem cerca de {Credito_Acumu:.2f}T credito acumulado seu saldo atualizado e de R$ {R:.2f}<<<<<<<<<<<<<<')
                while True:
                    P_2 = input('Responda Sim ou Não para a pergunta [2]: ').upper()
                    if P_2 != "SIM" and P_2 != "NAO":
                        print("DIGITE SIM OU NAO")
                    elif P_2 == "SIM":
                        Reduc = Reciclagem * Aterro_tempo
                        Taxa_Producao -= Reduc
                        Credito_Acumu = Taxa_BASELINE - Taxa_Producao
                        R += Credito_Acumu * 81.67
                        print(f'Com essa ação você acumulou cerca de {Credito_Acumu:.2f}T seu saldo atualizado e de R$ {R:.2f}')
                        while True:
                            P_3 = input('Responda Sim ou Não para a pergunta [3]: ').upper()
                            if P_3 != "SIM" and P_3 != "NAO":  
                                print("DIGITE SIM OU NAO")

                            elif P_3 == "SIM":
                                resposta = True
                                Reduc = Cobertura * Aterro_tempo
                                Taxa_Producao -= Reduc
                                Credito_Acumu = Taxa_BASELINE - Taxa_Producao
                                R += Credito_Acumu * 81.67
                                print(f'Com essa ação você acumulou cerca de {Credito_Acumu:.2f}T seu saldo atualizado e de R$ {R:.2f}')
                            elif P_3 == "NAO":
                                print(f'>>>>>>>>>Você tem cerca de {Credito_Acumu:.2f}T credito acumulado seu saldo atualizado e de R$ {R:.2f}<<<<<<<<<<<<<<')   
                            if resposta == True:
                                break    
                    elif P_2 == 'NAO':
                        resposta = True
                        print(f'>>>>>>>>>Você tem cerca de {Credito_Acumu:.2f}T credito acumulado seu saldo atualizado e de R$ {R:.2f}<<<<<<<<<<<<<<')     
                        while True:
                            P_3 = input('Responda Sim ou Não para a pergunta [3]: ').upper()
                            if P_3 != "SIM" and P_3 != "NAO":  
                                print("DIGITE SIM OU NAO")

                            elif P_3 == "SIM":
                                resposta = True
                                Reduc = Cobertura * Aterro_tempo
                                Taxa_Producao -= Reduc
                                R += Credito_Acumu * 81.67
                                print(f'Com essa ação você acumulou cerca de {Credito_Acumu:.2f}T seu saldo atualizado e de R$ {R:.2f}')
                            elif P_3 == "NAO":
                                print(Credito_Acumu)    
                            if resposta == True:
                                break    
                    if resposta == True:
                        break
            if resposta == True:
                break      
    elif select == 2:
        print("======================================================================================================================================================")
        print("""O cálculo de Oxido Nitroso e baseado em carros de aplicativos utilizados em Cidades Inteligentes, com base no modelo do carro, no Trafego 
e com algumas perguntas baseadas na queima de combustivel conseguimos criar uma previsão da quantidade de crédito que pode ser acumulada em um determinado
periodo.""")
        print("======================================================================================================================================================")
        SELECAO = ("""
======================> SELECIONE UM CARRO <======================
                              
[1] -> CHEVROLET ONIX
[2] -> HYUNDAI HB20
[3] -> VOLKSWAGEM GOL
                      
""")

        Anos = float(input("Digite a quantidade de Anos que você deseja simular a produção de Oxido Nitroso: "))
        Dias = Anos * 365
        Km_dia = float(input("Digite a quantidade de KM percorrida no dia: "))
        N_2_O = 0.0002
        conducao = 0.2 * N_2_O
        combustivel_QA = 0.4 * N_2_O
        Controle_Emissao = 0.8 * N_2_O
        N_2_0_Carbono = 298000
        Reais = 81.67
        ACUMULADO = 0

        while True:
            resposta = False
            print(SELECAO)

            Selecione = int(input('Digite o número do carro selecionado: '))

            if Selecione == 1:
                while True:
                    resposta = True
                    Trafego = print("""
                        [1] -> Baixo (14 KM/L)
                        [2] -> Normal (12 KM/L)
                        [3] -> Intenso (10 KM/L)
                        [0] -> Sair            
                                    """)
                    Trafego_selecao = int(input("Selecione o número que do Trafego: "))
                    if Trafego_selecao == 0:
                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                        break
                    elif Trafego_selecao == 1:
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 14
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                print("=============================================================================")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                print("=============================================================================")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha uma condução eficiente")
                                print("=============================================================================")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                print("=============================================================================")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print("=============================================================================")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 14
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        print("=============================================================================")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        print("=============================================================================")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso Combustivel de Qualidade")
                                        print("=============================================================================")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        print("=============================================================================")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print("=============================================================================")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        print("======================================RESPONDA SIM OU NÃO=======================================")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                print("=============================================================================")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print("=============================================================================")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                print("=============================================================================")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                print("=============================================================================")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print("=============================================================================")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                print("=============================================================================")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print("=============================================================================")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print("=============================================================================")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 14
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            elif P1 == "NÃO":           
                                resposta = True                
                                Km_l = 14
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 14
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            else:
                                                print("DIGITE SIM OU NÃO") 
                                                resposta = False   
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 14
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break

                    elif Trafego_selecao == 2:
                        resposta = True
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 12
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha uma condução eficiente")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 12
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 12
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            elif P1 == "NÃO":
                                resposta = True                
                                Km_l = 12
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 12
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 12
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break
                    elif Trafego_selecao == 3:
                        resposta = True
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 14
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha uma condução eficiente")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 10
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 10
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 10
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 10
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 10
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 10
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            elif P1 == "NÃO":
                                resposta = True                
                                Km_l = 10
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 10
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 10
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 10
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 10
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 10
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um Onix caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 10
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um Onix e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um Onix")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break
                    elif Trafego_selecao == 0:
                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                        break
            elif Selecione == 2:            
                while True:
                    resposta = True
                    Trafego = print("""
                        [1] -> Baixo (16 KM/L)
                        [2] -> Normal (13 KM/L)
                        [3] -> Intenso (11 KM/L)
                        [0] -> Sair            
                                    """)
                    Trafego_selecao = int(input("Selecione o número que do Trafego: "))
                    if Trafego_selecao == 0:
                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                        break
                    elif Trafego_selecao == 1:
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 16
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha uma condução eficiente")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 16
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 16
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 16
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 16
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 16
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 16
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            elif P1 == "NÃO":
                                resposta = True                
                                Km_l = 16
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 16
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 16
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 16
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 16
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 16
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 16
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break
                    elif Trafego_selecao == 2:
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 13
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha uma condução eficiente")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 13
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 13
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 13
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 13
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 13
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 13
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            elif P1 == "NÃO":
                                resposta = True                
                                Km_l = 13
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 13
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 13
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 13
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 13
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 13
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 13
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break
                    elif Trafego_selecao == 3:
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 11
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha uma condução eficiente")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 11
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 11
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 11
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 11
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 11
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 11
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            elif P1 == "NÃO":
                                resposta = True                
                                Km_l = 11
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 11
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 11
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 11
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 11
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 11
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um HB20 caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 11
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um HB20 e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um HB20")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break
                    elif Trafego_selecao == 0:
                        break    
            elif Selecione == 3:
                while True:
                    resposta = True
                    Trafego = print("""
                        [1] -> Baixo (17 KM/L)
                        [2] -> Normal (14 KM/L)
                        [3] -> Intenso (12 KM/L)
                        [0] -> Sair
                                    """)
                    Trafego_selecao = int(input("Selecione o número que do Trafego: "))
                    if Trafego_selecao == 0:
                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                        break
                    elif Trafego_selecao == 1:
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 17
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha uma condução eficiente")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 17
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 17
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 17
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 17
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 17
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 17
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            elif P1 == "NÃO":
                                resposta = True                
                                Km_l = 17
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 17
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 17
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 17
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 17
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 17
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 17
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break
                    elif Trafego_selecao == 2:
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 14
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha uma condução eficiente")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 14
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 14
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            elif P1 == "NÃO":
                                resposta = True                
                                Km_l = 14
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 14
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 14
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 14
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break
                    elif Trafego_selecao == 3:           
                        reducao = """
                                    (1) - O Veiculo tem condução eficiente?
                                    (2) - Combustivel de Qualdidade?
                                    (3) - O veiculo possui Tecnologias de Controle de Emissões?
                            """
                        print(reducao)
                        while True:
                            P1 = input("O Veiculo tem condução eficiente?: " ).upper()
                            if P1 != "SIM" and P1 != "NÃO":
                                print("DIGITE SIM OU NÃO")
                            if P1 == "SIM":
                                resposta = True
                                Km_l = 12
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                conducao_ano = conducao * Dias
                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - conducao_ano
                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha uma condução eficiente")
                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                Toneladas = Carbono_Reduzido / 1000
                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                Moeda = Toneladas * Reais
                                ACUMULADO += Moeda
                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 12
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 12
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break 
                                if resposta == True:
                                    break   
                            elif P1 == "NÃO":
                                resposta = True                
                                Km_l = 12
                                Litros_Dia = Km_dia / Km_l
                                Emisao_Dia = Litros_Dia * N_2_O
                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                Emisao_Anos = Emisao_Dia * Dias
                                Moeda = 0
                                ACUMULADO += Moeda
                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                while True:
                                    P2 = input("Combustivel de Qualdidade? " ) 
                                    if P2 != "SIM" and P2 != "NÃO":
                                        print("DIGITE SIM OU NÃO")
                                    elif P2 == "SIM":
                                        resposta = True
                                        Km_l = 12
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        combustivel_QA_ano = combustivel_QA * Dias
                                        Emisao_Anos_reduzido = (Emisao_Dia * Dias) - combustivel_QA_ano
                                        Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                        print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso Combustivel de Qualidade")
                                        Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                        Toneladas = Carbono_Reduzido / 1000
                                        print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                        Moeda = Toneladas * Reais
                                        ACUMULADO += Moeda
                                        print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                
                                    elif P2 == "NÃO":
                                        resposta = True                
                                        Km_l = 12
                                        Litros_Dia = Km_dia / Km_l
                                        Emisao_Dia = Litros_Dia * N_2_O
                                        print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                        Emisao_Anos = Emisao_Dia * Dias
                                        Moeda = 0
                                        ACUMULADO += Moeda
                                        print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                        print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                        print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                        while True:
                                            P3 = input("O veiculo possui Tecnologias de Controle de Emissões? ")
                                            if P3 != "SIM" and P3 != "NÃO":
                                                print("DIGITE SIM OU NÃO")
                                            elif P3 == "SIM":
                                                resposta = True
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                Controle_Emissao_ano = Controle_Emissao * Dias
                                                Emisao_Anos_reduzido = (Emisao_Dia * Dias) - Controle_Emissao_ano
                                                Credito_Carbono = Emisao_Anos - Emisao_Anos_reduzido
                                                print(f"Em {Anos} Anos Você deixara de produzir cerca de  {Credito_Carbono:.2f}kg Oxido Nitroso por um GOL caso tenha um bom controle de Emissão")
                                                Carbono_Reduzido = Credito_Carbono * N_2_0_Carbono
                                                Toneladas = Carbono_Reduzido / 1000
                                                print(f"Você terá cerca de {Carbono_Reduzido}kg de carbono não jogado na atmosfera, você terá cerca de  {Toneladas:.2f}T Credito de Carbono")
                                                Moeda = Toneladas * Reais
                                                ACUMULADO += Moeda
                                                print(f"Convertendo para Reais você terá cerca de R${Moeda:.2f}")
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}")
                                            elif P3 == "NÃO":
                                                resposta = True                
                                                Km_l = 12
                                                Litros_Dia = Km_dia / Km_l
                                                Emisao_Dia = Litros_Dia * N_2_O
                                                print(f"O valor de Oxido Nitroso emitido por dia com um GOL e de {Emisao_Dia}kg")
                                                Emisao_Anos = Emisao_Dia * Dias
                                                Moeda = 0
                                                ACUMULADO += Moeda
                                                print(f"Em {Anos} Anos será produzido um total de {Emisao_Anos:.2f}kg Oxido Nitroso por um GOL")
                                                print('Você deixou de produzir um total de 0.0 de Carbono na atmosfera')
                                                print(f"O valor acumulado e de R${ACUMULADO:.2f}") 
                                            if resposta == True:
                                                break                 
                                    if resposta == True:
                                        break    
                            if resposta == True:
                                break
                        if resposta == True:    
                            break    
            if resposta == True:    
                break          
    elif select == 3:

        print("""O cálculo de carbono e baseado em Árvores plantadas com mais de 20 anos para produzir crédito de carbono onde o usuario realiza somente a quantidade de Hectares onde está a árvore podendo repetir 3 vezes o cálculo""")
        arvores = {
            1: {"nome": "Mogno", "credito": 50},
            2: {"nome": "Eucalipto", "credito": 30},
            3: {"nome": "Carvalho", "credito": 40}
        }


        taxa_conversao = 86.71

        def calcular_creditos(arvore, hectares):
            if arvore in arvores:
                credito_por_hectare = arvores[arvore]["credito"]
                creditos = credito_por_hectare * hectares
                return creditos
            else:
                return None


        execucoes = 0
        total_creditos = 0
        hectares = float(input("Digite a quantidade de hectares: "))

        while execucoes < 3:
            print(f"Execução {execucoes + 1}")

            
        
            print("Escolha uma das opções de árvores (digite o número):")
            for numero, arvore_info in arvores.items():
                print(f"{numero}. {arvore_info['nome']}")


            escolha_numero = int(input("Digite o número da árvore escolhida: "))


            creditos_de_carbono = calcular_creditos(escolha_numero, hectares)

            if creditos_de_carbono is not None:
                total_creditos += creditos_de_carbono
                valor_em_reais = total_creditos * taxa_conversao
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(f"Você produzirá {creditos_de_carbono} créditos de carbono com {hectares} hectares de {arvores[escolha_numero]['nome']}.")
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(f"Valor total em reais: R$ {valor_em_reais:.2f}")
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            else:
                print("Árvore não encontrada.")

            execucoes += 1


        valor_em_reais = total_creditos * taxa_conversao
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(f"Total de créditos de carbono acumulados: {total_creditos}")
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(f"Valor total em reais: R$ {valor_em_reais:.2f}")
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print("Fim do programa.")
    elif select == 0:
        break