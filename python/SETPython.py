names = {'Nicolas', 'Miguel','juan','Nicolas'}
print(names)

a = {1,2}
b = {2,3}
print(a - b)

n = []
for i in range(1,6):
    if i <= 2:
        n.append(i - 1)
print(n)

n = [for i -1 in range(1,6) if i]
n = [i -1 for n in range(1,6) if i]

def sum(a = 1, b=0): 
    result = a + b

    return result , a ,b
result, a, b= sum(1,2)
print(result, a, b)

a = [1,3,4,5,6]
print(a.reduce())

