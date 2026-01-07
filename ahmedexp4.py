print("Ahmeed Farooqui")
print("UIN :- 251P090")

num1 = float(input("Entre the first number:"))
num2 = float(input("Entre the second number:"))

additio = num1+num2
subtraction = num1-num2
multiplication = num1*num2

if num2!=0:
    division = num1/num2
    modulus = num1%num2

print("\n Result of Arithmetic Operation:")
print(f"{num1}+{num2} = {additio}")
print(f"{num1}-{num2} = {subtraction}")
print(f"{num1}*{num2} = {multiplication}")
print(f"{num1}/{num2} = {division}")
print(f"{num1}%{num2} = {modulus}")