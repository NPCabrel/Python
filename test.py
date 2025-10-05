

import os

print("____________________________________________________________PASCAL NAGUE_____________________________________________________________________________")


#Implémenter une fonction personnalisée qui convertit une chaîne de caractères en minuscules,
#sans utiliser la méthode intégrée str.lower().

def lower1(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

if __name__ == "__main__":
    MyStrings= ["Hello World!", "PasCaL iS 27 YeaRs", "TESTING", "lowerCASE", "12345", "MiXeD CaSe"]
    for s in MyStrings:
        print(f"Original: {s} -> Lowercase: {lower1(s)}")
    

print("____________________________________________________________PASCAL NAGUE______________________________________________________________________________________")

os.system("pause")

# Pour convertir une chaîne en minuscules en Python sans utiliser la méthode lower(), vous pouvez 
# utiliser la fonction ord() pour obtenir la valeur ASCII d'un caractère et la fonction chr() pour
# obtenir le caractère correspondant à une valeur ASCII donnée. Les lettres majuscules ont des valeurs 
# ASCII comprises entre 65 (A) et 90 (Z), tandis que les lettres minuscules ont des valeurs entre 97 (a) 
# et 122 (z). Pour convertir une lettre majuscule en minuscule, il suffit d'ajouter 32 à sa valeur ASCII.