import re

# Texto y patrón
text = "The price is $45.00"
pattern = r'\$\d+\.\d+'

# Buscar coincidencias
matches = re.findall(pattern, text)

# Mostrar coincidencias
print(matches)
