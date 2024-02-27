# On cherche à écrire une fonction pour obtenir de l’usager un nombre dans un certain intervalle. Si le
# nombre entré n’est pas dans l’intervalle en question, il faut continuer à demander à l’usager d’entrer un
# nombre dans cet intervalle jusqu’à ce qu’un nombre valide soit entré.
# Faire la conception de cette fonction en répondant aux 5 questions de conception de fonction vues en cours

def get_number_in_interval_from_user(min, max):
    num = min - 1
    while num > max or num < min:
        num = float(input('Entrez un nombre entre ' + str(min) + ' et ' + str(max) + ': '))

if __name__ == '__main__':
    get_number_in_interval_from_user(0, 100)

# 1. obtenir de l’usager un nombre dans un certain intervalle
# 2. min et max, 2 integers
# 3. retourne None 
# 4. get_number_in_interval_from_user
# 5. ex: get_number_in_interval_from_user(0, 100)