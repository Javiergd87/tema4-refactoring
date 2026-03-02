# Refactorización aplicada:
# - Rename Method
# - Extract Method
# - Eliminación de código duplicado
# - Reorganización de condicionales


def calcular_media(nota1, nota2, nota3):
    """Calcula la media de tres notas."""
    return (nota1 + nota2 + nota3) / 3


def evaluar_media(media):
    """Devuelve el mensaje correspondiente según la media."""
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspendido"


def main():
    nota1 = 4
    nota2 = 6
    nota3 = 8

    media = calcular_media(nota1, nota2, nota3)
    resultado = evaluar_media(media)

    print(resultado)


if __name__ == "__main__":
    main()