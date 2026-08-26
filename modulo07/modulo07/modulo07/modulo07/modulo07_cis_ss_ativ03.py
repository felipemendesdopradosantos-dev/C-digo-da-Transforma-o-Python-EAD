# Jogo de Adivinhação que é 24 Números e 
# tem 6 chances para acertar o número secreto.

import random
import math

numeros = list(range(1, 25))
numero_secreto = random.choice(numeros)

max_tentativas = 6
tentativas = 0

print("🎮 ===============================")
print("🎯   JOGO DO NÚMERO SECRETO")
print("🎮 ===============================")
print("🔢 Existem 24 números possíveis!")
print("❤️ Você tem 6 chances para acertar!")
print("🍀 Boa sorte!\n")

while tentativas < max_tentativas:
    print(f"❤️ Chances restantes: {max_tentativas - tentativas}")
    palpite = int(input("👉 Digite seu palpite (1 a 24): "))

    if palpite < 1 or palpite > 24:
        print("⚠️ Digite um número entre 1 e 24!\n")
        continue

    tentativas += 1
    diferenca = math.fabs(numero_secreto - palpite)

    if palpite == numero_secreto:
        print("\n🎉 PARABÉNS!")
        print(f"🏆 Você acertou o número secreto: {numero_secreto}")
        print(f"🎯 Você precisou de {tentativas} tentativa(s)!")
        break
    elif palpite < numero_secreto:
        print("📈 Tente um número MAIOR!")
    else:
        print("📉 Tente um número MENOR!")

    if diferenca <= 3:
        print("🔥 Você está MUITO perto!")
    elif diferenca <= 6:
        print("🙂 Você está perto!")
    else:
        print("🥶 Você está longe!")

    print()

if tentativas == max_tentativas and palpite != numero_secreto:
    print("💀 FIM DE JOGO!")
    print(f"😢 Você utilizou todas as {max_tentativas} chances.")
    print(f"🔐 O número secreto era: {numero_secreto}")
    print("🎮 Tente novamente!")