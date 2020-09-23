import string
simbolos='0123456789'+string.ascii_letters
import sys,random
tamanho=int(sys.argv[1])
def randchar():
    qnt_simbolos=len(simbolos)
    return simbolos[random.randrange(0,qnt_simbolos)]
texto=''.join([randchar() for i in range(tamanho)])
print(texto)
    
