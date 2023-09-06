file = 'text'
ext =  '.txt'
filename = f'{file}{ext}'
permiso = 'r+'
print(filename) 
with open(f'./{filename}', f'{permiso}') as file:
        print(f'./{filename}')
        for line in file:
            print(line)
        file.write('Nuevas lineas\n')
        file.read()
    