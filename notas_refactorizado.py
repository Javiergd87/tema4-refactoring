"""
notas_refactorizado.py

Programa de refactorización de cálculo de medias de notas.
Autor: Javier G.
Fecha: 02/03/2026

Este programa calcula la media de tres notas de un alumno y devuelve
una calificación categórica (Sobresaliente, Notable, Aprobado, Suspendido).
"""


def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres notas.

    Args:
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.

    Returns:
        float: La media de las tres notas (valor entre 0 y 10).
    """
    return (nota1 + nota2 + nota3) / 3


def evaluar_media(media):
    """
    Evalúa la media obtenida y devuelve la calificación correspondiente.

    Args:
        media (float): Media calculada de las tres notas.

    Returns:
        str: Calificación según la media:
            - "Sobresaliente" si media >= 9
            - "Notable" si 7 <= media < 9
            - "Aprobado" si 5 <= media < 7
            - "Suspendido" si media < 5
    """
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspendido"


def main():
    """
    Función principal del programa.

    Define las notas de un alumno, calcula la media y muestra
    la calificación correspondiente en pantalla.
    """
    nota1 = 4
    nota2 = 6
    nota3 = 8

    # Calculamos la media usando la función calcular_media
    media = calcular_media(nota1, nota2, nota3)

    # Obtenemos la calificación usando evaluar_media
    resultado = evaluar_media(media)

    print(resultado)  # Mostramos la calificación final del alumno


if __name__ == "__main__":
    main()