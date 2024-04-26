#Projeto 1 - Algoritmos e Programação 1
#Integrantes:
#Matheus Tramont Hoffmann

import time
import math
#Introduzindo variáveis:
SupxProp = 0
SupyProp = 0
InfxProp = 0
InfyProp = 0
SupxEdif = 0
SupyEdif = 0
InfxEdif = 0
InfyEdif = 0
contador1 = 0
contador2 = 0
contador3 = 0
distancia = 0
angulo = 0
#Definindo a função do menu, o loop principal que se repete indefinitivamente e apresenta opções que levam para outras funções do código.
def menu():
        while True:
            print("Análise de Chuva de Meteoros")
            print("1. Definir perímetro da propriedade e da edificação de interesse")
            print("2. Definir localização da UPMCC e unificar sistemas de coordenadas de referência")
            print("3. Processar registros de chuva de meteoros")
            print("4. Apresentar estatísticas da última chuva processada")
            print("5. Sair")
            opção = int(input("Escolha sua opção: "))

            if opção == 1:
                opção1()
            elif opção == 2:
                opção2()
            elif opção == 3:
                #A função opção3() depende das funções opção1() e opção2() para funcionar. Portanto elas devem ser executadas antes dessa função.
                if (contador1 == 0 or contador2 == 0):
                        print("[ERRO] Defina os perímetros da propriedade e da edificação e a localização da UPMCC primeiro.")
                #Ela também depende da sincronização de usos destas duas funções para que os sistemas referenciais estejam unificados e os resultados sejam coerentes.
                elif (contador1 == contador2):
                        opção3()
                else:
                        print("[ERRO] Unifique os sistemas referenciais.")
            elif opção == 4:
                #A função opção4() precisa que a função opção3() tenha sido executada ao menos uma vez, caso o contrário não retornará resultados.
                if contador3 > 0:
                        opção4()
                else:
                        print("[ERRO] Nenhuma chuva de meteoros processada.")
            elif opção == 5:
                #Esta opção quebra o loop e encerra o programa.
                print("Saindo do sistema...")
                time.sleep(1)
                break
            else:
                print("Opção inválida.")
                
#Definindo a função opção1(). Ela obtém o input das coordenadas dos pontos da propriedade e da edificação, que serão usadas em outras funções do código.
def opção1():
        #Tornando as variáveis globais, para que possam ser utilizadas nessa e em outras funções.
        global SupxProp
        global SupyProp
        global InfxProp
        global InfyProp
        global SupxEdif
        global SupyEdif
        global InfxEdif
        global InfyEdif
        global contador1
        SupxProp = float(input("Defina o eixo horizontal do ponto superior esquerdo da propriedade: "))
        SupyProp = float(input("Defina o eixo vertical do ponto superior esquerdo da propriedade: "))
        InfxProp = float(input("Defina o eixo horizontal do ponto inferior direito da propriedade: "))
        InfyProp = float(input("Defina o eixo vertical do ponto inferior direito da propriedade: "))
        SupxEdif = float(input("Defina o eixo horizontal do ponto superior esquerdo da edificação: "))
        SupyEdif = float(input("Defina o eixo vertical do ponto superior esquerdo da edificação: "))
        InfxEdif = float(input("Defina o eixo horizontal do ponto inferior direito da edificação: "))
        InfyEdif = float(input("Defina o eixo vertical do ponto inferior direito da edificação: "))
        #Contador para verificar quantas vezes a função foi executada.
        contador1 = contador1 + 1

#Definindo a opção2(). Ela obtém mais duas variáveis, sendo essas as coordenadas do ponto da UPMCC, e com base nelas translada o valor das coordenadas da opção1().
def opção2():
        #Globalizando o valor das variáveis introduzidas nessa função, que também serão utilizadas em outra função do código.
        global Basex
        global Basey
        Basex = float(input("Defina o eixo horizontal do ponto da UPMCC: "))
        Basey = float(input("Defina o eixo vertical do ponto da UPMCC: "))
        #Globalizando os valores das variáveis da opção1() nesta função, para que seus valores estejam atualizados ao serem utilizadas na próxima função.
        global SupxProp
        global SupyProp
        global InfxProp
        global InfyProp
        global SupxEdif
        global SupyEdif
        global InfxEdif
        global InfyEdif
        global contador2
        SupxProp = SupxProp - Basex
        SupyProp = SupyProp - Basey
        InfxProp = InfxProp - Basex
        InfyProp = InfyProp - Basey
        SupxEdif = SupxEdif - Basex
        SupyEdif = SupyEdif - Basey
        InfxEdif = InfxEdif - Basex
        InfyEdif = InfyEdif - Basey
        #Contador para verificar quantas vezes a função foi executada.
        contador2 = contador2 + 1

#Definindo a função opção3(). Ela recebe valores indefinitivamente, e com esses valores cria dados para serem utilizados na próxima função.
def opção3():
        #Globalizando as variáveis introduzidas nessa função, para serem utilizadas nesta ou na próxima função.
        global distancia
        global angulo
        global contadora
        global meteorx
        global meteory
        global contador3
        global quedaspropriedade
        global quedasedificio
        global quadranteNE
        global quadranteNO
        global quadranteSO
        global quadranteSE
        #Introduzindo variáveis contadoras:
        contadora = 0
        contadorprop = 0
        quadranteNE = 0
        quadranteNO = 0
        quadranteSO = 0
        quadranteSE = 0
        quedaspropriedade = 0
        #Esta variável é uma exceção, pois é uma string que deve ter seu estado base como "NÃO", e apenas será modificada se o meteoro cair dentro do perímetro do edifício de interesse.
        quedasedificio = "NÃO"
        print("Para encerrar o registro, digite uma distância negativa.")
        #Loop que deve durar indefinitivamente, obtendo inputs sobre as coordenadas de meteoros, até que o usuário digite um número negativo no input da variável distancia.
        while True:
                #Contadora para saber o número de meteoros registrados.
                contadora = contadora + 1
                print("Registro #",contadora, sep='')
                distancia = float(input("Informe a distância do meteoro em relação a base: "))
                if distancia < 0:
                        break
                angulo = float(input("Informe o ângulo em relação ao eixo polar: "))
                #As coordenadas polares são convertidas para cartesianas.
                meteorx = round(distancia * math.cos(math.radians(angulo)), 2)
                meteory = round(distancia * math.sin(math.radians(angulo)), 2)
                #As coordenadas do meteoro são transladadas com base no ponto da UPMCC.
                meteorx0 = meteorx + Basex
                meteory0 = meteory + Basey
                #Essa cadeia de if-elif-else verifica as coordenadas de cada meteoro, checando se o meteoro caiu dentro da propriedade e, nesse caso, em qual quadrante ele caiu.
                if SupxProp < meteorx and SupyProp > meteory and InfxProp > meteorx and InfyProp < meteory:
                        quedaspropriedade = quedaspropriedade + 1
                        if meteorx0 > 0 and meteory0 > 0:
                                quadranteNE = quadranteNE + 1
                                propriedade = " dentro da propriedade, no quadrante NE."
                        elif meteorx0 < 0 and meteory0 > 0:
                                quadranteNO = quadranteNO + 1
                                propriedade = " dentro da propriedade, no quadrante NO."
                        elif meteorx0 < 0 and meteory0 < 0:
                                quadranteSO = quadranteSO + 1
                                propriedade = " dentro da propriedade, no quadrante SO."
                        elif meteorx0 > 0 and meteory0 < 0:
                                quadranteSE = quadranteSE + 1
                                propriedade = " dentro da propriedade, no quadrante SE."
                else:
                        propriedade = " fora da propriedade."
                #Este if checa se o meteoro caiu dentro da edificação de interesse, e muda o valor da variável mencionada como exceção anteriormente.
                if SupxEdif < meteorx and SupyEdif > meteory and InfxEdif > meteorx and InfyEdif < meteory:
                        quedasedificio = "SIM"
                #Print informando ao usuário alguns dados sobre o meteoro recém-processado.
                print("O meteoro caiu no ponto (",meteorx,";", meteory,") com origem na UPMCC, ou no ponto (",meteorx0,";",meteory0,") com origem no ponto (0;0),", propriedade,sep='') 
        #Ajuste da contadora, descontando o último meteoro que foi desconsiderado.
        contadora = contadora - 1
        print("Fim da coleta de registros:", contadora, "queda(s) informada(s).")
        #Contador de quantas vezes a função foi executada.
        contador3 = contador3 + 1

#Definindo a função opção4(). Ela simplesmente coleta os dados da última função e calcula e mostra estatísticas para o usuário.
def opção4():
        print("Total de quedas registradas:",contadora)
        print("Quedas dentro da propriedade: ",quedaspropriedade, " (",round((quedaspropriedade/contadora)*100, 2),"% do total de quedas)",sep='')
        print("> Quadrante NE: ",quadranteNE, " (",round((quadranteNE/quedaspropriedade)*100, 2),"% das quedas na propriedade)",sep='')
        print("> Quadrante NO: ",quadranteNO, " (",round((quadranteNO/quedaspropriedade)*100, 2),"% das quedas na propriedade)",sep='')
        print("> Quadrante SO: ",quadranteSO, " (",round((quadranteSO/quedaspropriedade)*100, 2),"% das quedas na propriedade)",sep='')
        print("> Quadrante SE: ",quadranteSE, " (",round((quadranteSE/quedaspropriedade)*100, 2),"% das quedas na propriedade)",sep='')
        print("A edificiação principal foi atingida?",quedasedificio)
 
menu()    
