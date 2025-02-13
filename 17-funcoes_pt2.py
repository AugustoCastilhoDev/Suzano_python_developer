def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado (a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")
    
exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)


print("____________________________________")


salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)
print(f"O novo salário é: {salario_com_bonus}")