num1 = float(input("Digite o primeiro numero: "))
op = input("Digite o operador: ")
num2 = float(input("Digite o segundo numero: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Operador invalido")
