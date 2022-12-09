# Definimos una función que tome una cadena de caracteres y devuelva un diccionario con las subcadenas y su puntuación
def minion_game(string):
  # Creamos un diccionario vacío que almacenará las subcadenas y su puntuación
  substrings = {}
  
  # Iteramos sobre todas las letras de la cadena
  for i in range(len(string)):
    # Stuart forma palabras que comiencen con consonantes
    if string[i] not in "AEIOU":
      # Iteramos sobre todas las subcadenas que comiencen con la letra actual
      for j in range(i + 1, len(string) + 1):
        # Agregamos la subcadena al diccionario y aumentamos su puntuación en 1
        substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1
        
    # Kevin forma palabras que comiencen con vocales
    else:
      # Iteramos sobre todas las subcadenas que comiencen con la letra actual
      for j in range(i + 1, len(string) + 1):
        # Agregamos la subcadena al diccionario y aumentamos su puntuación en 1
        substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1s
  return substrings
# Probamos la función con la cadena "BANANA"

print(minion_game("BANANA"))
