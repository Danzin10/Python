def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Conversor de Unidades de Temperatura")
    print("Escolha a conversão:")
    print("1: Celsius para Fahrenheit")
    print("2: Fahrenheit para Celsius")

    escolha = input("Digite o número da sua escolha (1 ou 2): ")

    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
    
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
    
    else:
        print("Escolha inválida!")

if __name__ == "__main__":
    main()
