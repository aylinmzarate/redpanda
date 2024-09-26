import argparse

# Crear el parser
parser = argparse.ArgumentParser(description='Un script que imprime un mensaje con el nombre y la edad proporcionados.')

# Añadir argumentos
parser.add_argument('name', type=str, help='El nombre de la persona.')
parser.add_argument('age', type=int, help='La edad de la persona.')

# Parsear los argumentos
args = parser.parse_args()

# Usar los argumentos
print(f"Hola, {args.name}! Tienes {args.age} años.")
