simbolos='0123456789'
import sys,random
tamanho=int(sys.argv[1])
def randchar():
    qnt_simbolos=len(simbolos)
    return simbolos[random.randrange(0,qnt_simbolos)]
texto=''.join([randchar() for i in range(tamanho)])
print(texto)
    
