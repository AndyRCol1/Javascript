#Expresiones regulares
import re

text = "5Hola4 como6 estas"

result = re.findall('[0-9]', text)
print(result)

# manipulacion de fecjas
import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result,' ',local,' ' ,timestamp)
# Frecuencia de datos
import collections
numbers= [1,2,3,1,2,4,5,6,7,8,5,6,3,4,7]
counter = collections.Counter(numbers)
print(counter)