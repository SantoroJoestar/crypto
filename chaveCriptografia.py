# APS - ATIVIDADES PRÁTICAS SUPERVISIONADAS
# SecureCrypto - Software com o propósito de oferecer um sistema de criptografia

#Função que usa a chave de Criptografia das mensagens
def chaveCriptografar(fraseCriptografada):
    mensagemCriptografada = "" #Variável que ira armanezar a mensagem já criptografada    
    #Letras e caracteres especiais

    for letra in fraseCriptografada:
        if letra in "Aa":
            mensagemCriptografada = mensagemCriptografada + "f"
        elif letra in "Bb":
            mensagemCriptografada = mensagemCriptografada + "k"
        elif letra in "Cc":
            mensagemCriptografada = mensagemCriptografada + "h"
        elif letra in "Dd":
            mensagemCriptografada = mensagemCriptografada + "q"
        elif letra in "Ee":
            mensagemCriptografada = mensagemCriptografada + "s"
        elif letra in "Ff":
            mensagemCriptografada = mensagemCriptografada + "v"
        elif letra in "Gg":
            mensagemCriptografada = mensagemCriptografada + "u"
        elif letra in "Hh":
            mensagemCriptografada = mensagemCriptografada + "b"
        elif letra in "Ii":
            mensagemCriptografada = mensagemCriptografada + "j"
        elif letra in "Jj":
            mensagemCriptografada = mensagemCriptografada + "m"
        elif letra in "Kk":
            mensagemCriptografada = mensagemCriptografada + "p"
        elif letra in "Ll":
            mensagemCriptografada = mensagemCriptografada + "x"
        elif letra in "Mm":
            mensagemCriptografada = mensagemCriptografada + "c"
        elif letra in "Nn":
            mensagemCriptografada = mensagemCriptografada + "z"
        elif letra in "Oo":
            mensagemCriptografada = mensagemCriptografada + "i"
        elif letra in "Pp":
            mensagemCriptografada = mensagemCriptografada + "n"
        elif letra in "Qq":
            mensagemCriptografada = mensagemCriptografada + "w"
        elif letra in "Rr":
            mensagemCriptografada = mensagemCriptografada + "l"
        elif letra in "Ss":
            mensagemCriptografada = mensagemCriptografada + "g"
        elif letra in "Tt":
            mensagemCriptografada = mensagemCriptografada + "a"
        elif letra in "Uu":
            mensagemCriptografada = mensagemCriptografada + "t"
        elif letra in "Vv":
            mensagemCriptografada = mensagemCriptografada + "o"
        elif letra in "Ww":
            mensagemCriptografada = mensagemCriptografada + "e"
        elif letra in "Xx":
            mensagemCriptografada = mensagemCriptografada + "y"
        elif letra in "Yy":
            mensagemCriptografada = mensagemCriptografada + "d"
        elif letra in "Zz":
            mensagemCriptografada = mensagemCriptografada + "r"
        elif letra in "Çç":
            mensagemCriptografada = mensagemCriptografada + "$"
        elif letra in " ":
            mensagemCriptografada = mensagemCriptografada + "+-*/"
        elif letra in ",":
            mensagemCriptografada = mensagemCriptografada + "."
        elif letra in ".":
            mensagemCriptografada = mensagemCriptografada + ","
        
        #Números
        
        elif letra in "1":
            mensagemCriptografada = mensagemCriptografada + "5"
        elif letra in "2":
            mensagemCriptografada = mensagemCriptografada + "3"
        elif letra in "3":
            mensagemCriptografada = mensagemCriptografada + "1"
        elif letra in "4":
            mensagemCriptografada = mensagemCriptografada + "4"
        elif letra in "5":
            mensagemCriptografada = mensagemCriptografada + "9"
        elif letra in "6":
            mensagemCriptografada = mensagemCriptografada + "6"
        elif letra in "7":
            mensagemCriptografada = mensagemCriptografada + "0"
        elif letra in "8":
            mensagemCriptografada = mensagemCriptografada + "2"
        elif letra in "9":
            mensagemCriptografada = mensagemCriptografada + "7"
        elif letra in "0":
            mensagemCriptografada = mensagemCriptografada + "8"
        
        #Acentos

        elif letra in "Ãã":
            mensagemCriptografada = mensagemCriptografada + "õ"
        elif letra in "Ââ":
            mensagemCriptografada = mensagemCriptografada + "ê"
        elif letra in "Áá":
            mensagemCriptografada = mensagemCriptografada + "é"    
        elif letra in "Àà":
            mensagemCriptografada = mensagemCriptografada + "è"
        elif letra in "Éé":
            mensagemCriptografada = mensagemCriptografada + "í"    
        elif letra in "Êê":
            mensagemCriptografada = mensagemCriptografada + "î"
        elif letra in "Èè":
            mensagemCriptografada = mensagemCriptografada + "ì"
        elif letra in "Íí":
            mensagemCriptografada = mensagemCriptografada + "ó"
        elif letra in "Îî":
            mensagemCriptografada = mensagemCriptografada + "ô"  
        elif letra in "Ìì":
            mensagemCriptografada = mensagemCriptografada + "ò"  
        elif letra in "Õõ":
            mensagemCriptografada = mensagemCriptografada + "ã"
        elif letra in "Ôô":
            mensagemCriptografada = mensagemCriptografada + "û"    
        elif letra in "Óó":
            mensagemCriptografada = mensagemCriptografada + "ú"
        elif letra in "Òò":
            mensagemCriptografada = mensagemCriptografada + "ù"
        elif letra in "Ûû":
            mensagemCriptografada = mensagemCriptografada + "â"
        elif letra in "Úú":
            mensagemCriptografada = mensagemCriptografada + "á"
        elif letra in "Ùù":
            mensagemCriptografada = mensagemCriptografada + "à"
        else:
            mensagemCriptografada = mensagemCriptografada + letra
    return mensagemCriptografada

