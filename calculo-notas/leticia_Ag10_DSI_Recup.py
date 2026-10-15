def calcular_medias(notas : list) -> float|None:
    if notas == []:   
        return None
    return (sum(notas)/ len(notas))  

def aprov_reprov(notas : list, nota_aprov : float) -> str: 
    if calcular_medias(notas) >= nota_aprov:
        return "aprovado"
    else:
        return "reprovado"

def relatorio(nome, nota_aprov, notas):
    medias = calcular_medias(notas)
    if medias == None:
        print(f"O aluno/a {nome} não tem nenhuma nota.")
    else:
        print(
            f"O aluno/a {nome} teve uma média de {medias:.2f}\n "
            f"e foi {aprov_reprov(notas, nota_aprov)}!\n"
            f"pois a nota mínima para ser aprovado é de {nota_aprov}."
        )

nome = input("qual o seu nome ")
notas = []
while True:
    try:
        nota_aprov = float(
            input("Qual a nota mínima para aprovação? ").replace(",", ".")
        )
        break
    except ValueError:
        print("Não foi possível, digite um número.")

while True:
    entrada = input("Digite sua nota ou uma letra para calcular a média: ")

    try:
        nota = float(entrada.replace(",", "."))
    except ValueError:
        break

    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Digite uma nota entre 0 e 10.")

relatorio(nome, nota_aprov, notas)