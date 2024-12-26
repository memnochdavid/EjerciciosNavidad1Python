import string


def alphaToNum(letra: str):
    inicio = ord('a')
    return ord(letra.lower()) - inicio + 1


def numToAlpha(numero: int):
    inicio = ord('a')
    return chr(numero + inicio - 1)


def agrupar_en_bloques(lista, n):
    return [lista[i:i + n] for i in range(0, len(lista), n)]


def cifra_mensaje(mensaje: str, k: int):
    # Eliminamos signos de puntuación y espacios
    mensaje_trim = ''.join(letra for letra in mensaje if letra not in string.punctuation and not letra.isspace())
    aux1 = []
    cifrado = []

    for letra in mensaje_trim:
        aux1.append(alphaToNum(letra))

    bloques = agrupar_en_bloques(aux1, k)
    for bloque in bloques:
        bloque_cifrado = '-'.join(str(num) for num in bloque)
        cifrado.append(bloque_cifrado)

    return cifrado


def descifra_mensaje(cifrado: list, k: int):
    mensaje = ""

    for bloque in cifrado:
        nums = [int(num) for num in bloque.split('-')]
        for num in nums:
            mensaje += numToAlpha(num)
    return mensaje

#ejecuta
mensaje = "Feliz Navidad!"
k = 3

cifrado = cifra_mensaje(mensaje, k)

print("Cifrado Navideño 😄")
print("Mensaje original: ", mensaje)
print("Cifrado: ", cifrado)

descifrado = descifra_mensaje(cifrado, k)

print("Descifrado: ", descifrado)
