"""
                        Exercicio 01 Aula 05
    Escreva uma função que calculeo fatorial de um 
    número recebido como  parâmentro e retorne o seu
    resultado

    *faça uma validação dos dados por  meio de uma  outra
     função, permitindo  que somente  valores positivos sejam
     aceito

    *Crie o help da sua função(exercicio)                       
"""

def fatorial(num):
    """
    Efetua o fatorial de um numero solicitado 
    return num
    """
    fat =1
    if num == 0:
        return fat
    
    for i in range(1,num+1,1):
        fat*=i
     
          
    return fat
res=fatorial(8)
print(res)

