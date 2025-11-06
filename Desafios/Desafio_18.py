import math
# Caso precise pedir um angulo, substituir a variável angulo por: angulo = float(input("Digite um ângulo: "))
angulo = float(input("Digite um ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {:.0f}º, tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.".format(angulo, seno, cosseno, tangente))

