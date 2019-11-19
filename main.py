""" importe les modules nécessaires aux trois fonctions """
import argparse

from api import lister_parties, débuter_partie, jouer_coup

def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('-l', '--lister', metavar='',help="Lister les identifiants de vos 20 dernières parties")
    parser.add_argument('idul', help='IDUL du joueur')
    return parser.parse_args()

def afficher_damier_ascii(dico):
    nom1 = str(dico['joueurs'][0]['nom'])
    nom2 = str(dico['joueurs'][1]['nom'])
    print(f"Légende : 1={nom1}, 2={nom2}")
    print('   -----------------------------------')
    damier1 = [[' ' for i in range(39)] for j in range(17)]
    for i, j in enumerate(damier1[::2]):
        j[0] = str(9 - i)
        for x in range(4, 39, 4):
            j[x] = '.'
    liste = []
    for j in damier1:
        j[2] = j[38] = '|'
        liste = liste + j + ['\n']
    position1 = dico['joueurs'][0]['pos']
    x1, y1 = position1[0], position1[1]
    position2 = dico['joueurs'][1]['pos']
    x2, y2 = position2[0], position2[1]
    joueur1 = 40*(18 - 2*y1) + 4*x1
    joueur2 = 40*(18 - 2*y2) + 4*x2
    liste[joueur1] = str(1)
    liste[joueur2] = str(2)
    horizontaux = dico["murs"]["horizontaux"]
    for j in horizontaux:
         x = (j[0])
         y = (j[1])
         for i in range(7):
             liste[40*(18 - 2*y) + 4*x + 39 + i] = '-'
    verticaux = dico["murs"]["verticaux"]
    for j in verticaux:
        x = (j[0])
        y = (j[1])
        liste[40*(18 - 2*y) + 4*x - 2] = liste[40*(18 - 2*y) + 4*x - 42] =  liste[40*(18 - 2*y) + 4*x - 82] = '|'
    liste.pop()
    chaine = ''.join(liste)
    print(chaine)
    print('--|-----------------------------------')
    print('  | 1   2   3   4   5   6   7   8   9')

d = débuter_partie(analyser_commande().idul)
if len(d) > 1:
    a = d[1]
    afficher_damier_ascii(a)
    gagnant = True
    while gagnant: 
        type_cout = input('Entrez le coup que vous voulez faire ')
        position = input('Entrez la position ') 
        e = jouer_coup(d[0], type_cout, position)
        if e.get('message'):
            afficher_damier_ascii(a)
            print(e['message'])
        elif e.get('gagnant'):
            gagnant = False
            winner = e['gagnant']
            print(f"Le gagnant est : {winner}")
        else:
            a = e['état']
            afficher_damier_ascii(a)

else:
    print(d['message'])