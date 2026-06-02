def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas numericas.

    Argumentos:
    notas -- lista de enteros o flotantes

    Retorna:
    float -- el promedio calculado
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


# Cambio de verificación para Pull Request