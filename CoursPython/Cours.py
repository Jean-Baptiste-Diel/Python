# Mise a niveau Python

# Les variables
age = 18
nom = "INANG"
prenom = "Diel"
disponible = True

# La fonction type()  permet de déterminer le type d’une variable
print(type(age))

# Les conditions
if not disponible:
    texte = "disponible pour une balade"
else:
    texte = "indisponible pour une balade"

# Affichage
print(f"Je m'appelle {nom} {prenom}, j'ai {age} ans et je suis {texte}")

# Les listes
print("------ les listes ------")
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
print(plateformes_sociales[1])
# Pour connaitre la taille de la liste on utilise len()
print(f"Taille de la liste est: {len(plateformes_sociales)}")
# Pour trie une liste on utise .sorted() cela cree une nouvelle liste
x = sorted(plateformes_sociales)
print(x)
# Acceder a un elements d'une chaine
lettre = "Jean Baptiste"
print(lettre[0])
# Modifier un element d'une liste grace a son index
plateformes_sociales[2] = "Linkedn"
print(plateformes_sociales)
# Pour ajouter on utile .append()
plateformes_sociales.append("Telegram")
print(plateformes_sociales)
# Pour supprimer c'est .remove()
plateformes_sociales.remove("Facebook")
print(plateformes_sociales)

# Les tuples, la difference avec une liste est que les tuples sont immuables
print("------ les tuples ------")
plateformes_sociales_tuple = ("Facebook", "Instagram", "TikTok", "Twitter")
print(plateformes_sociales_tuple)
# Pour savoir si un element est present  dans un tuple ou une liste
var = "Facebook" in plateformes_sociales_tuple
print(var)

# Les dictionnaires
print("------ les dictionnaires ------")
# Creation d'un dictionnaire
# Methode n01 avec la fonction dict()
film1 = dict()
film1["nom"] = "Titanic"
film1["duree"] = "2 heures"
print(film1)
# Methode n02 avec les {}
film2 = {'nom': ("Le roi lion",), 'duree': "2h40"}
# Acceder a un element grace a sa cle
print(film2['nom'])
# Ajouter une nouvelle cle - valeur
film2['Acteurs'] = "Morgan FREEMAN"
print(film2)
# Supprimer une cle - valeur on utilse del
del film2['Acteurs']
print(film2)
var = "livre" in film2
print(var)

# Les boucles
print("------ les boucles ------")
# La boucles for
personnes = ["John", "Smith", "Don"]
print("------ la boucle for ------")
for personne in personnes:
    print(personne)
i = 0
print("------ la boucles while ------")
while i < 5:
    print(i)
    i += 1


# Les fonction
def addition():
    return 5 + 50
