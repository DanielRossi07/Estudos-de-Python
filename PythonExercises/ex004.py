algo = input("Digite algo:")
print(type(algo))
print("Somente números:", algo.isnumeric())  # Todos números
print("Somente números e letras:", algo.isalnum())  # Todos números ou letras
print("Somente letras:", algo.isalpha())  # Todos letras
print("Somente números decimais:", algo.isdecimal())  # Todos decimais
print("Somente digitos do 1 ao 9:", algo.isdigit())  # Todos digitos
print("Somente letras minusculas:", algo.islower())  # Todos minusculos
print("Somente espaços em branco:", algo.isspace())  # Todos espaços em branco
print("Primeira letra em CAPS e outras pequenas:", algo.istitle())  #
print("Somente letras em CAPS:", algo.isupper())  # Todos casplock
