import random
import json

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

players = []
rounds = 0
score1 = 0
score2 = 0

def main():
    # definire une liste vide ,remplire la liste avec des tasses et pierres aléatoirement et faire appelle au fonction.
    global players
    global rounds
    global score1
    global score2

    with open('players.json') as f:
        players_dict = json.load(f)

    for player_dict in players_dict:
        player = Player(player_dict["name"], player_dict["score"])
        players.append(player)

    liste = []
    randtasse = random.randint(3, 7)
    randpierre = random.randint(5, 23)
    nom1, nom2 = avoir_joueurs()

    for n in [x for x in players if x.name == nom1]:
        score1 = n.score
        print(" {}  a deja jouer et son score est: {}".format(nom1, score1))



    for n in [x for x in players if x.name == nom2]:
        score2 = n.score
        print("{} a deja jouer et son score est: {}".format(nom2, score2))


    joueur = nom1 
                  # initialiser le joueur qui joue en 1 (on le changera plus tard)
    
    commencer_jeu(liste, randtasse, randpierre, joueur) # initialiser le jeux

    final(liste, randtasse, randpierre, nom1, nom2, joueur) 

# statut : ne prend pas d'arguments et retourne les noms des joueurs comme des chaines de caractère entrés par l'utilisateur          
def avoir_joueurs():
    return input("donner le nom du 1er joueur:  "), input("donner le nom du 2eme joueur:  ")

# il prend une liste vide, un nombre de tasse et de pierre aléatoire, et les noms des joueurs comme chaine de caractère
# elle fait entrer les parametres et commence le jeux 
def commencer_jeu(liste, randtasse, randpierre, joueur):

    
    print("amuser-vous!!")
    print("-" * 25)
    for i in range(0, randtasse):
        randpierre = random.randint(5, 23)
        _r = 23 - randpierre
        print(' {}| {} {}'.format(i + 1, '*' * randpierre, ' ' * _r) ,'|',randpierre)

        liste.append(randpierre)  
    print("-" * 25)

    

# vérification des valeurs et leurs type entrés par l'utilisateur et affiche un message d'erreur au cas ou. 
def verif_valid_entres(liste, randtasse, joueur):

    # le boucle qui verifie les parametres entrés 
    while True:
        
        tasse = input('{},choisit une tasse :' .format(joueur))
        pierres = input('{}, commbien du pierre tu veux prendre? '.format(joueur))

        # si toutes les conditions sont verifies on sort de la boucle .
        if (pierres and tasse) and (pierres.isdigit()) and (tasse.isdigit()):
            if (int(pierres) > 0) and (int(tasse) <= len(liste)) and (int(tasse) > 0):
                if (int(pierres) <= liste[int(tasse) - 1]):
                    if (int(pierres) != 0) and (int(tasse) != 0):
                        break
        
        # sinon afficher ce message
        print("Hmmm. tu as donner une mauvaise valeur,essayer une autre fois, {}.".format(joueur))
        
    # mise à jour du jeu
    liste[int(tasse) - 1] -= int(pierres)

    # continuation du jeu
    continue_game(liste, randtasse, joueur)

# il prend une liste vide, un nombre de tasse et de pierre aléatoire, et les noms des joueurs comme chaine de caractère
# elle fait entrer les parametres et continuer le jeux apres les modification 
def continue_game(liste, randtasse, joueur): 
    global rounds
    rounds += 1
    print("Regardons le tableau maintenant.")
    print("-" * 25)
    for i in range(0, randtasse):
        _r = 23 - liste[i]
        print(" {} | {} {}".format(i + 1, '*' * liste[i], ' ' * _r),'|', liste[i])
         
    print("-" * 25)

    #affichage de la liste 


def final(liste, randtasse, randpierre, nom1, nom2, joueur):
    global players
    global rounds

    
    while True :
        verif_valid_entres(liste, randtasse, joueur)
        
        # determiner le gagnant !!!
        if liste == [0] * len(liste):
            if joueur == nom1:
               joueur = nom2

            else:
             joueur = nom1


            score = 0
            _s = 0
            for x in range(1, rounds):
              score += x * (10 ** x)

            print("{} tu as gagné !!!, votre score est: {}".format(joueur, score))

            _winner_exists = False
            for player in players:
                if player.name == joueur:
                    _winner_exists = True
                    if player.score == 0:
                        player.score = score
                    else:
                        if score < player.score:
                            player.score = score

            if not _winner_exists:
                players.append(Player(joueur, score))

            if joueur == nom1:
                loser = nom2
            else:
                loser = nom1

            _loser_exists = False
            for player in players:
                if player.name == loser:
                    _loser_exists = True

            if not _loser_exists:
                players.append(Player(loser, 0))


            with open('players.json', 'w') as results:
                json.dump([player.__dict__  for player in players], results)


            break
            
        # changement du joueurs 2->1, 1->2 
        if joueur == nom1:
            joueur = nom2

        else:
            joueur = nom1


main()
