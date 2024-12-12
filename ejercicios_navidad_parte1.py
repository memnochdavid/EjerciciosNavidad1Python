#ejercicio01
import random


def arbol_navidad(n)->str:
    arbol=""
    aux=0
    for i in range(1, n+1):
        for j in range(1, (n + 1) - i):
            arbol += " "
        for j in range(1, i):
            arbol += "*"
        for j in range(1, i + 1):
            arbol += "*"
        aux+=1
        arbol += "\n"
    aux=aux-(aux//3)
    arbol+=" "*aux
    arbol+="|"*4
    return arbol

#ejercicio02
def filtrar_regalos(regalos, letra):
    return [regalo for regalo in regalos if regalo[0]==letra]

#ejercicio03
def contar_bolas(lista, tam):
    return [bola for bola in lista if bola>=tam]

#ejercicio04
def sorteo_navidad(regalos, gente)->list:
    random.shuffle(regalos)
    random.shuffle(gente)
    lista=[]
    for i in range(0, len(regalos)):
        lista.append(gente[i])
        lista.append(regalos[i])
    return lista
    


#ejercicios
stop=False
while not stop:
    ejercicio=int(input("HO-HO-HO! Ejercicio a ejecutar:"))
    match ejercicio:
        case 1:
            print(arbol_navidad(9))
        case 2:
            letra="R"
            lista=("Patines", "Raquteta", "Muñeco", "Peonza", "Cometa","Perrito","Ropa", "Rosa")
            print(filtrar_regalos(lista,letra))
        case 3:
            tamanio=5
            lista_bolas=(3,4,5,3,7,9,6,43,2,67,8,3)
            print(contar_bolas(lista_bolas, tamanio))
        case 4:
            regalos=["Patines", "Guantes", "Trineo", "Muñeco", "Playboy"]
            gente=["Juanito", "Jaimito", "Jorgito", "Pepito", "Albertito"]
            print(f"Los regalos y sus dueños son: {str(sorteo_navidad(regalos, gente))}")
        case 5:
