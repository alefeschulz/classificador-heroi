# Classificador de nível - Python

nome_do_heroi = input("Digite o nome do herói: ")
xp_do_heroi = int(input("Digite a quantidade de XP: "))

if xp_do_heroi < 1000:
    nivel = "Ferro"
elif xp_do_heroi <= 2000:
    nivel = "Bronze"
elif xp_do_heroi <= 5000:
    nivel = "Prata"
elif xp_do_heroi <= 7000:
    nivel = "Ouro"
elif xp_do_heroi <= 8000:
    nivel = "Platina"
elif xp_do_heroi <= 9000:
    nivel = "Ascendente"
elif xp_do_heroi <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

print(f"O Herói de nome {nome_do_heroi} está no nível de {nivel}")
