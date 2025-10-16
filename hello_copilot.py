def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        print(f"Calculating fibonacci for n = {n}")
        return 1
    else:
        print(f"Calculating fibonacci for n = {n}")
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def main():
    import sys
    print("=== Calculadora de Fibonacci ===")
    print("Nota: Para números mayores a 50, el cálculo puede tardar mucho tiempo.")
    sys.stdout.flush()  # Forzar la salida
    
    while True:
        try:
            # Solicitar entrada al usuario
            n = input("Ingrese un número para calcular Fibonacci (o 'q' para salir): ")
            sys.stdout.flush()  # Forzar la salida
            
            # Verificar si el usuario quiere salir
            if n.lower() == 'q':
                print("¡Hasta luego!")
                break
            
            # Convertir a entero
            n = int(n)
            
            # Validar que sea un número positivo
            if n < 0:
                print("Por favor, ingrese un número entero no negativo.")
                continue
            
            # Advertencia para números grandes
            if n > 50:
                respuesta = input(f"¿Estás seguro de calcular Fibonacci({n})? Puede tardar mucho (s/n): ")
                if respuesta.lower() != 's':
                    continue
            
            # Calcular y mostrar el resultado
            print(f"Calculando Fibonacci({n})...")
            resultado = calculate_fibonacci(n)
            print(f"El número de Fibonacci en la posición {n} es: {resultado}")
            print("-" * 40)
            
        except ValueError:
            print("Por favor, ingrese un número válido o 'q' para salir.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

# Funcion que analiza un listado de emails y retorna los que son validos
# def filter_valid_emails(emails):
#     import re
#     import requests
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     valid_emails = [email for email in emails if re.match(pattern, email)]
#     return valid_emails
# 
#     def get_pokemon_data(pokemon_name):
#         
#         url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
#         
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f"Error al consultar Pokemon: {e}")
#             return None