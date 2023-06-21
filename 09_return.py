# parametros por defecto
def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth, width, 'Hola desde volume'

result, width, text = find_volume(width=10)

print(result, width, text)