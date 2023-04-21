import re

while True:
    password = input("Veuillez choisir un mot de passe: ")
    if len(password) < 8:
        print("Erreur: Le mot de passe doit contenir au moins 8 caractères.")
    elif not re.search("[a-z]", password):
        print("Erreur: Le mot de passe doit contenir au moins une lettre minuscule.")
    elif not re.search("[A-Z]", password):
        print("Erreur: Le mot de passe doit contenir au moins une lettre majuscule.")
    elif not re.search("[0-9]", password):
        print("Erreur: Le mot de passe doit contenir au moins un chiffre.")
    elif not re.search("[!@#$%^&*]", password):
        print("Erreur: Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
    else:
        print("Le mot de passe est valide.")
        break

import hashlib

password = input("Veuillez choisir un mot de passe: ")
hash_object = hashlib.sha256(password.encode())
hex_dig = hash_object.hexdigest()
print("Le mot de passe crypté est:", hex_dig)