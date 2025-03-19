# Calculadora de Factorial
# Autor: Duban Andrés López
# Licencia: MIT License - Este código es libre y puede ser modificado y distribuido.

def factorial(n):
    """Calcula el factorial de un número positivo."""
    if n < 0:
        return "El número debe ser positivo"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

if __name__ == "__main__":
    num = int(input("Ingrese un número positivo: "))
    print(f"El factorial de {num} es: {factorial(num)}")
