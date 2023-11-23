
def jogar():
    print("Jogo da Forca:")

    palavra_secreta = "banana"
    palavra_mostrada = palavra_secreta.count
    enforcou = False
    acertou = False
    tentativas = 3
    while (not enforcou and not acertou):
        print("Você tem {} tentativas!".format(tentativas))
        chute = input("Digite uma letra:")
        errou = False
        for letra in palavra_secreta:
            if(chute == letra):
                errou = False
                break
            else:
                errou = True
                

        if (errou):
            print("Não tem a letra!")
            tentativas = tentativas - 1
        else:
            print("tem a letra!!")
            
        if(tentativas == 0):
            enforcou = True
            print("Voce não conseguiu! Enforcou!")
            break

    
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()



