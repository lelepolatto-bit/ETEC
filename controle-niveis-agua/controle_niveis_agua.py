from colorama import Fore, Style, init

init(autoreset=True)

mensagens = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

cores = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE
]

def exibir_nivel(nivel):
    if nivel < 1 or nivel > len(mensagens):
        print("Nível inválido.")
    else:
        indice = nivel - 1
        print(cores[indice] + mensagens[indice])

nivel_atual = 3

print("=== Monitoramento do Reservatório ===")
exibir_nivel(nivel_atual)
