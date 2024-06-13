


cont = 0
matriculas = []

# Recebe o número inicial da matrícula e a quantidade de matrículas a copiar
mat = int(input("Digite a partir de qual matricula vc quer buscar: "))
contador = int(input("Digite quantas matriculas voce quer copiar: "))

# Loop para incrementar e salvar as matrículas
while cont < contador:
    cont += 1
    mat += 1
    matriculas.append(mat)

# Converte a lista de matrículas em uma tupla
matriculas_tupla = tuple(matriculas)

# Exibe as matrículas no formato de tupla
print(f"Matrículas: {matriculas_tupla}")
