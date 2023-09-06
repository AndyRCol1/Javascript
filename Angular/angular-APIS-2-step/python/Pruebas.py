#declaro varibles
#name = input("Cual es tu nombre ?") || "Andres";
name = "Andres";
lastName = "Rodriguez";
Edad = 27;
Skill = "SQL Sever - Develoment";
objeto = { 1 ,2,3}
print(objeto);
#lanzo un msj
print ("Yo soy " + name
       + " "+ lastName
       + " "+ "tengo "
       + str(Edad)
       + " años, Soy Experto en "
       + Skill );
Edad += 1
template = f"Yo soy {name} y tengo {Edad} años"
print(template);
for x in name:
  print(x + " " + lastName)
# tipo de datos

print ("Esta variable es de tipo ", type(name))

# objetos

obj = {
  'name': "Andres",
  'lastName': "Rodriguez",
  'age': "27",
}
print(obj)
print(obj['age'])
print(obj['name'])

###reto
dictionary = {"key1":"value1", "key2":"value2", "key3":"value3"}
print(dictionary)

dictionary["key4"] = "value4"
print(dictionary)

