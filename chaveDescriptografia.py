# APS - ATIVIDADES PRÁTICAS SUPERVISIONADAS
# SecureCrypto - Software com o propósito de oferecer um sistema de criptografia

#Função que usa a chave de Descriptografia das mensagens
def chaveDecriptografar(fraseDecriptografada):
    mensagem_decriptografada = "" #Variável que ira armanezar a mensagem já descriptografada
    #Letras e caracteres especiais
    for mensagem_criptografada in fraseDecriptografada:
        if mensagem_criptografada in "f":
            mensagem_decriptografada = mensagem_decriptografada + "a"
        elif mensagem_criptografada in "k":
            mensagem_decriptografada = mensagem_decriptografada + "b"
        elif mensagem_criptografada in "h":
            mensagem_decriptografada = mensagem_decriptografada + "c"
        elif mensagem_criptografada in "q":
            mensagem_decriptografada = mensagem_decriptografada + "d"
        elif mensagem_criptografada in "s":
            mensagem_decriptografada = mensagem_decriptografada + "e"
        elif mensagem_criptografada in "v":
            mensagem_decriptografada = mensagem_decriptografada + "f"
        elif mensagem_criptografada in "u":
            mensagem_decriptografada = mensagem_decriptografada + "g"
        elif mensagem_criptografada in "b":
            mensagem_decriptografada = mensagem_decriptografada + "h"
        elif mensagem_criptografada in "j":
            mensagem_decriptografada = mensagem_decriptografada + "i"
        elif mensagem_criptografada in "m":
            mensagem_decriptografada = mensagem_decriptografada + "j"
        elif mensagem_criptografada in "p":
            mensagem_decriptografada = mensagem_decriptografada + "k"
        elif mensagem_criptografada in "x":
            mensagem_decriptografada = mensagem_decriptografada + "l"
        elif mensagem_criptografada in "c":
            mensagem_decriptografada = mensagem_decriptografada + "m"
        elif mensagem_criptografada in "z":
            mensagem_decriptografada = mensagem_decriptografada + "n"
        elif mensagem_criptografada in "i":
            mensagem_decriptografada = mensagem_decriptografada + "o"
        elif mensagem_criptografada in "n":
            mensagem_decriptografada = mensagem_decriptografada + "p"
        elif mensagem_criptografada in "w":
            mensagem_decriptografada = mensagem_decriptografada + "q"
        elif mensagem_criptografada in "l":
            mensagem_decriptografada = mensagem_decriptografada + "r"
        elif mensagem_criptografada in "g":
            mensagem_decriptografada = mensagem_decriptografada + "s"
        elif mensagem_criptografada in "a":
            mensagem_decriptografada = mensagem_decriptografada + "t"
        elif mensagem_criptografada in "t":
            mensagem_decriptografada = mensagem_decriptografada + "u"
        elif mensagem_criptografada in "o":
            mensagem_decriptografada = mensagem_decriptografada + "v"
        elif mensagem_criptografada in "e":
            mensagem_decriptografada = mensagem_decriptografada + "w"
        elif mensagem_criptografada in "y":
            mensagem_decriptografada = mensagem_decriptografada + "x"
        elif mensagem_criptografada in "d":
            mensagem_decriptografada = mensagem_decriptografada + "y"
        elif mensagem_criptografada in "r":
            mensagem_decriptografada = mensagem_decriptografada + "z"
        elif mensagem_criptografada in "$":
            mensagem_decriptografada = mensagem_decriptografada + "ç"
        elif mensagem_criptografada in "+-*/":
            mensagem_decriptografada = mensagem_decriptografada + " "
        elif mensagem_criptografada in ",":
            mensagem_decriptografada = mensagem_decriptografada + "."
        elif mensagem_criptografada in ".":
            mensagem_decriptografada = mensagem_decriptografada + ","
        elif mensagem_criptografada in "$":
            mensagem_decriptografada = mensagem_decriptografada + "ç"

        #Números

        elif mensagem_criptografada in "5":
            mensagem_decriptografada = mensagem_decriptografada + "1"
        elif mensagem_criptografada in "3":
            mensagem_decriptografada = mensagem_decriptografada + "2"
        elif mensagem_criptografada in "1":
            mensagem_decriptografada = mensagem_decriptografada + "3"
        elif mensagem_criptografada in "4":
            mensagem_decriptografada = mensagem_decriptografada + "4"
        elif mensagem_criptografada in "9":
            mensagem_decriptografada = mensagem_decriptografada + "5"
        elif mensagem_criptografada in "6":
            mensagem_decriptografada = mensagem_decriptografada + "6"
        elif mensagem_criptografada in "0":
            mensagem_decriptografada = mensagem_decriptografada + "7"
        elif mensagem_criptografada in "2":
            mensagem_decriptografada = mensagem_decriptografada + "8"
        elif mensagem_criptografada in "7":
            mensagem_decriptografada = mensagem_decriptografada + "9"
        elif mensagem_criptografada in "8":
            mensagem_decriptografada = mensagem_decriptografada + "0"


        #Acentos

        elif mensagem_criptografada in "õ":
            mensagem_decriptografada = mensagem_decriptografada + "ã"
        elif mensagem_criptografada in "ê":
            mensagem_decriptografada = mensagem_decriptografada + "â"
        elif mensagem_criptografada in "é":
            mensagem_decriptografada = mensagem_decriptografada + "á"    
        elif mensagem_criptografada in "è":
            mensagem_decriptografada = mensagem_decriptografada + "à"
        elif mensagem_criptografada in "í":
            mensagem_decriptografada = mensagem_decriptografada + "é"    
        elif mensagem_criptografada in "î":
            mensagem_decriptografada = mensagem_decriptografada + "ê"
        elif mensagem_criptografada in "ì":
            mensagem_decriptografada = mensagem_decriptografada + "è"
        elif mensagem_criptografada in "ó":
            mensagem_decriptografada = mensagem_decriptografada + "í"
        elif mensagem_criptografada in "ô":
            mensagem_decriptografada = mensagem_decriptografada + "î"  
        elif mensagem_criptografada in "ò":
            mensagem_decriptografada = mensagem_decriptografada + "ì"  
        elif mensagem_criptografada in "ã":
            mensagem_decriptografada = mensagem_decriptografada + "õ"
        elif mensagem_criptografada in "û":
            mensagem_decriptografada = mensagem_decriptografada + "ô"    
        elif mensagem_criptografada in "ú":
            mensagem_decriptografada = mensagem_decriptografada + "ó"
        elif mensagem_criptografada in "ù":
            mensagem_decriptografada = mensagem_decriptografada + "ò"
        elif mensagem_criptografada in "â":
            mensagem_decriptografada = mensagem_decriptografada + "û"
        elif mensagem_criptografada in "á":
            mensagem_decriptografada = mensagem_decriptografada + "ú"
        elif mensagem_criptografada in "à":
            mensagem_decriptografada = mensagem_decriptografada + "ù"    
        else:
            mensagem_decriptografada = mensagem_decriptografada + mensagem_criptografada
    return mensagem_decriptografada
