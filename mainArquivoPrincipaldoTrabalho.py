# APS - ATIVIDADES PRÁTICAS SUPERVISIONADAS
# SecureCrypto - Software com o propósito de oferecer um sistema de criptografia

#
#Programa Principal: 
#

#Importando as funções criadas para criptografar e descriptografar
from chaveCriptografia import chaveCriptografar
from chaveDescriptografia import chaveDecriptografar

frase = "" #Variável que ira armazenar as frases criptografadas e descriptografadas
#fraseCriptografada = "" #Parametro

#Variáveis das mensagens pré programadas
primeiraMsgCriptografada='f+-*/qjgaêzhjf+-*/gsutlf+-*/nflf+-*/gs+-*/inslfl+-*/ig+-*/bsxjhúnaslig+-*/qi+-*/zfoji.+-*/í+-*/qs+-*/58pc.'
segundaMsgCriptografada = 'f+-*/qjgaêzhjf+-*/gsutlf+-*/qi+-*/zfoji+-*/nflf+-*/f+-*/higaf+-*/í+-*/qs+-*/98pc'
primeiraMsgDescriptografada = 'Uma segunda equipe está sendo enviada para ajudar no local.'
###

max = 128 #Máximo de caracteres que podem ser usados nas frases
frasesFinais = '' #Frases usadas a vontade no final do programa

#Ambiente inicial do programa
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
print("                                                   SecureCrypto                                                    ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
print("Capitão da Guarda Costeira Brasileira: ", "Inspetor, irei lhe passar as informações do que está acontecendo. ")
print(" ")
print("A situação é a seguinte, um navio foi apreendido por transportar lixo tóxico, destinado ao norte do Brasil. ")
print(" ")
print("Sendo assim, precisamos manter todo o cuidado possível, e para apenas inspetores devidamente trajados devem adentrar ao local, e a troca de informações e mensagens será totalmente criptografada, recebida e enviada apenas por você!")
resposta=input("Para isso precisamos que mantenha a calma e siga as instrução. Entendido? (Digite Sim para continuar, ou digite Não para repetir a mensagem.)")

#Estrutura condicional das respostas do usuário
while (resposta != "sim") or (resposta != "Sim"):
    if (resposta == "não") or (resposta == "Não"):
        print ("Ok vou repetir")
        print(" ")
        print("Capitão da Guarda Costeira Brasileira: ", "Inspetor, irei lhe passar as informações do que está acontecendo.")
        print(" ")
        print("A situação é a seguinte, um navio foi apreendido por transportar lixo tóxico, destinado ao norte do Brasil. ")
        print(" ")
        print("Sendo assim, precisamos manter todo o cuidado possível, e para apenas inspetores devidamente trajados devem adentrar ao local, e a troca de informações e mensagens será totalmente criptografada, recebida e enviada apenas por você!")
        resposta=input("Para isso precisamos que mantenha a calma e siga as instrução. Entendido? (Digite Sim para continuar, ou digite Não para repetir a mensagem.)")
    elif (resposta == "Sim") or (resposta == "sim"):
        print("-------------------------------- ")
        print("Ótimo, vamos continuar!")
        print("--------------------------------")
        break
    elif ((resposta != "Sim") or (resposta != "sim")) or ((resposta != "Não") or (resposta != "não")):
        resposta = input("Não entendi sua resposta, tente novamente: ")
        print('----------------------------------------------------------------')

print("Todas as mensagens serão criptografadas, vc já conhece o método, iremos lhe passar uma mensagem agora: ", primeiraMsgCriptografada)
#print(chaveDecriptografar(frase)) #Método/Função de Descriptografar
frase = input("Digite a frase (Copie e cole a mensagem, para facilitar.)")
qtdCaracteresFrase = len(frase)

#Primeiro exemplo de Descriptografia
while (frase != primeiraMsgCriptografada or qtdCaracteresFrase > max):
    print("------------------------------------------------------------------------------------------------")
    frase = input("Mensagem errada, por favor digite a mensagem que lhe foi passada: ")
    if (frase != primeiraMsgCriptografada):
        continue
    break
print("---------------------------------------------------------------------------------------------------------")
print("Ótimo, mensagem descriptografada:")
print(chaveDecriptografar(frase))
print("---------------------------------------------------------------------------------------------------------")        
print("Muito bem, uma última mensagem será enviada, e logo depois você ira criptografar as mensagens! ")
print("--------------------------------------------------------------------------------------------------------- ")
print("Por favor, descriptografe a mensagem: ", segundaMsgCriptografada)
print("---------------------------------------------------------------------------------------------------------")
#Segundo exemplo de descriptografia
frase = input("Digite a frase (Copie e cole a mensagem, para facilitar.)")
print("---------------------------------------------------------------------------------------------------------")
qtdCaracteresFrase = len(frase)
while (frase != segundaMsgCriptografada or qtdCaracteresFrase > max):
    frase = input("Mensagem errada, por favor digite a mensagem que lhe foi passada: ")
    print("---------------------------------------------------------------------------------------------------------")
    if (frase != segundaMsgCriptografada):
        continue
    break
print("------------------------------------------------------------------------------------------------------------------------------")
print("Ótimo, mensagem descriptografada:")
print("------------------------------------------------------------------------------------------------------------------------------")
print(chaveDecriptografar(frase))
print("------------------------------------------------------------------------------------------------------------------------------ ")
print("Excelente Inspetor! Agora ficará responsável de mandar as mensagens criptografadas, vamos começar!")
print("------------------------------------------------------------------------------------------------------------------------------")
print("Muito bem, por favor me criptografe a seguinte mensagem: ",primeiraMsgDescriptografada)
print("------------------------------------------------------------------------------------------------------------------------------")
#Exemplo de Criptografia
frase = input("Digite a frase (Copie e cole a mensagem, para facilitar.)")
qtdCaracteresFrase = len(frase)
print(" ")
while (frase != primeiraMsgDescriptografada or qtdCaracteresFrase > max):
    frase = input("Mensagem errada, por favor digite a mensagem que lhe foi passada: ")
    if (frase != primeiraMsgDescriptografada):
        continue
    break
print("--------------------------------")
print("Ótimo, mensagem criptografada:")
print(chaveCriptografar(frase))
print("--------------------------------")

#Ambiente livre de testes
print("A situação inteira já foi criada, você já aprendeu a usar o sistema, sinta-se livre para testar a vontade as funções de criptografar e de descriptografar.")
print("--------------------------------------------------------------------------------------------------------------------------------")
resposta = input("Você gostaria de continuar operando o programa, e testando as funções? Digite Sim para continuar, e Não para sair.") 
print("--------------------------------------------------------------------------------------------------------------------------------")
while (resposta != "sim") or (resposta != "Sim"):
    if (resposta == "não" or resposta == "Não"):
        print("--------------------------------")
        print("Fim da execução do programa.")
        print("--------------------------------")
        quit()
    if (resposta == "sim" or resposta == "Sim"):
        print("--------------------------------")
        print("Ótimo, vamos continuar")
        print("--------------------------------")
        break
    elif ((resposta != "Sim") or (resposta != "sim")) or ((resposta != "Não") or (resposta != "não")):
        print("--------------------------------------------------------")
        resposta = input("Não entendi sua resposta, tente novamente: ")
        print("--------------------------------------------------------")
#Escolha livre do usuário        
print("Gostaria de Criptografar ou Descriptografar? Digite C para criptografar, ou D para descriptografar.")
print(" ")
print("Para descriptografar, é necessário ter uma mensagem criptografada antes, recomendamos que criptografe quantos textos quiser, e depois utilize a função de descriptografar.")
resposta = input("Vamos prosseguir. Digite (C) para criptografar e (D) para descriptografar, ou escolha (X) para encerrar o programa: ")
qtdCaracteresFrase = len(frasesFinais)
while (resposta != "X" or resposta != "x"): 
    if (resposta == "X" or resposta == "x"):
        print("--------------------------------------------------------- ")
        print("Fim da execução do programa! Obrigado pela avaliação!!!")
        print("--------------------------------------------------------- ")
        exit()
    if (resposta == "C" or resposta == "c"):
        frasesFinais = input("Digite a frase que deseja criptografar:")
        print("--------------------------------------------------------- ")
        if (len(frasesFinais) > max):
            frasesFinais = input("A frase ultrapassa o limite de caracteres permitidos, por favor digite outra: ")
        print("Mensagem criptografada: ")
        print("--------------------------------------------------------- ")
        print(chaveCriptografar(frasesFinais)) 
    if (resposta == "D" or resposta == "d"): 
        print("--------------------------------------------------------- ")
        frasesFinais = input("Digite a frase que deseja descriptografar: ")
        if (len(frasesFinais) > max):
            frasesFinais = input("A frase ultrapassa o limite de caracteres permitidos, por favor digite outra: ")
        print("Mensagem descriptografada: ")
        print("--------------------------------------------------------- ")
        print(chaveDecriptografar(frasesFinais))
    if (resposta != "C" or resposta != "c" or resposta != "D" or resposta != "d" or resposta != "X" or resposta != "x" ):
        print()
        resposta = input("Digite sua opção novamente: ")
        continue
    
    ########### FIM DO PROGRAMA ###########
    
            