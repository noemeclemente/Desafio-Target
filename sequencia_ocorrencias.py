def contar_as(texto):
    """Conta o número de ocorrências da letra 'a' (maiúscula ou minúscula) em uma string.

    Args:
        texto: A string a ser analisada.

    Returns:
        O número de ocorrências da letra 'a'.
    """

    return texto.lower().count('a')

# Exemplo de uso:
texto = input("Digite um texto: ")
num_as = contar_as(texto)
print(f"A letra 'a' aparece {num_as} vezes no texto.")