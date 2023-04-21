import json
import hashlib

def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)

def load_passwords():
    try:
        with open("passwords.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def add_password(passwords):
    while True:
        website = input("Veuillez entrer le nom du site web: ")
        username = input("Veuillez entrer votre nom d'utilisateur: ")
        password = input("Veuillez entrer votre mot de passe: ")
        hashed_password = hash_password(password)
        if website in passwords:
            print("Un mot de passe pour ce site web est déjà enregistré.")
        else:
            passwords[website] = {"username": username, "password": hashed_password}
            save_passwords(passwords)
            print("Le mot de passe a été enregistré avec succès.")
            break

def display_passwords(passwords):
    if not passwords:
        print("Aucun mot de passe n'est enregistré.")
    else:
        for website, data in passwords.items():
            print(f"Site web: {website}, Nom d'utilisateur: {data['username']}, Mot de passe: {data['password']}")

passwords = load_passwords()

while True:
    action = input("Que voulez-vous faire ? Ajouter un nouveau mot de passe (a) ou afficher les mots de passe enregistrés (d) ? ")
    if action == "a":
        add_password(passwords)
    elif action == "d":
        display_passwords(passwords)
    else:
        print("Commande invalide.")
