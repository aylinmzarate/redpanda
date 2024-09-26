import subprocess

# Ejecutar un comando del sistema en Windows
result = subprocess.run('dir', capture_output=True, text=True, shell=True)

# Mostrar la salida del comando
print(result.stdout)
