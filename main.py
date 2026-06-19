# ===========================
#           VARIAVEIS
# ============================

saude = 1
inteligencia = 1
arcana = 1
disciplina = 1

jogador = {
    "nick": "Keylor",
    "nivel": 1,
    "xp": 0,

    "saude": 1,
    "inteligencia": 1,
    "arcana": 1,
    "disciplina": 1,
    "vitalidade": 1,
    "criatividade": 1
}

habitos = {
    "Estudar": {
        "xp": 10,
        "inteligencia": 1
    },

    "Programar": {
        "xp": 15,
        "arcana": 1,
        "inteligencia": 1,
    },

    "Treinar": {
        "xp": 20,
        "saude": 2,
        "vitalidade": 1,
    },

    "Arrumar a cama": {
        "xp": 5,
        "disciplina": 1
    },

    "Comer saudável": {
        "xp": 10,
        "saude": 1
    }
}

# =============================
# SALVAR DADOS
# =============================

def salvar_dados():
    with open("save.txt", "w") as arquivo:
        arquivo.write(f"{jogador['nivel']}\n")
        arquivo.write(f"{jogador['xp']}\n")

# ===========================
#   CARREGAR DADOS
# ===========================

def carregar_dados():
    global nivel, xp

    try:
        with open("save.txt", "r") as arquivo:
            nivel = int(arquivo.readline())
            xp = int(arquivo.readline())

    except FileNotFoundError:
        nivel = 1
        xp = 0

def ganhar_xp(valor: object) -> None:
    jogador["xp"] += valor
    print(f"\n+{valor} XP ganho!")
    verificar_level_up(
    )
    salvar_dados()

def verificar_level_up():
    xp_necessaria = jogador["nivel"] * 100

    if jogador["xp"] >= xp_necessaria:

        titulo_antigo = titulo_jogador()
        jogador["xp"] -= xp_necessaria
        jogador["nivel"] += 1

        print(f"\n Voce subiu para o nivel {jogador['nivel']}!\n")

        titulo_novo = titulo_jogador()

        if titulo_antigo != titulo_novo:
            print("\n===========================")
            print(" ✨ Novo título desbloqueado! ")
            print(f"{jogador['nivel']}, {titulo_novo}")
            print("=========================")
            print(
                f"\n🔥 {jogador['nick']}, {titulo_jogador()}, "
                f"subiu para o nível {jogador['nivel']}!"
            )
        salvar_dados()


def titulo_jogador():
    if jogador["nivel"] < 5:
        return "O Novato"
    elif jogador["nivel"] < 10:
        return "O Aprendiz"
    else:
        return "O Desperto"


def mostrar_status():
        xp_necessaria = nivel * 100
        print("\n===========STATUS==========")
        print(f"{jogador["nick"]}, {titulo_jogador()}")
        print(f"Nivel: {nivel}")
        print(f"XP: {xp}/{xp_necessaria}")
        print("=========================\n")

def mostrarNivel():
    global nivel
    print("\n=========NIVEL==========")
    print(f"Nivel: {nivel}")



def registrar_habito(nome_habito):
    dados = habitos[nome_habito]

    jogador["xp"] += dados["xp"]

    print(f"+{dados['xp']} XP")
    return dados

print(jogador["xp"])
registrar_habito("Treinar")

print(jogador["xp"])


def menu():
    while (True):
        print("1- Estudar(+10 XP")
        print("2- Fazer exercício(+20 XP")
        print("3- Fazer projeto(+50 XP")
        print("4- Ver status")
        print("5- Sair")

        escolha = input("Escolha:")

        if escolha == "1":
           ganhar_xp(10)
        elif escolha == "2":
             ganhar_xp(20)
        elif escolha == "3":
             ganhar_xp(50)
        elif escolha == "4":
             mostrar_status()
        elif escolha == "5":
            print(mostrarNivel())
        elif escolha == "6":
             print("Saindo...")
             break
        else:
          print("Opcao invalida!\n")



carregar_dados()
menu()
print(mostrarNivel())
