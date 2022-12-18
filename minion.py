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
        kevin=substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1
        
    # Kevin forma palabras que comiencen con vocales
    else:
      # Iteramos sobre todas las subcadenas que comiencen con la letra actual
      for j in range(i + 1, len(string) + 1):
        # Agregamos la subcadena al diccionario y aumentamos su puntuación en 1
        stuart=substrings[string[i:j]] = substrings.get(string[i:j], 0) + 1

  # Si la puntuación de Kevin es mayor que la de Stuart, Kevin gana
  if kevin>stuart:
    print("Kevin ",kevin)
  # Si la puntuación de Stuart es mayor que la de Kevin, Stuart gana
  elif stuart>kevin:
    print("Stuart ",stuart)
  # Si la puntuación de Kevin y Stuart es igual, es un empate
  else:
    print("Empate")

  return "\n"
# Probamos la función con la cadena "BANANA"


if __name__ == '__main__':

  print(minion_game('CARACOL'))
  print(minion_game('BANANA'))
