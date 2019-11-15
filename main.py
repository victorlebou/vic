import argparse
def analyser_commande():
    idul = input('Entrez votre idul')
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument('-l', '--lister', metavar='',help="Lister les identifiants de vos 20 dernières parties")
    parser.add_argument('idul', metavar= 'idul', help='IDUL du joueur')
    return parser.parse_args()

def afficher_damier_ascii(dico):
    nom1 = dico['joueurs'][0]['nom']
    nom2 = dico['joueurs'][1]['nom']
    f"Légende : 1={nom1}, 2={nom2}"
    damier = [[' ' for i in range(38)] for j in range(20)]
    damier[0] =   list('   -----------------------------------')
    damier[18] = list('--|-----------------------------------')
    damier[19] = list('  | 1   2   3   4   5   6   7   8   9')
    damier[1] = list('9 | .   .   .   .   .   .   .   .   . |')
    damier[3] = list('8 | .   .   .   .   .   .   .   .   . |')
    damier[5] = list('7 | .   .   .   .   .   .   .   .   . |')
    damier[7] = list('6 | .   .   .   .   .   .   .   .   . |')
    damier[9] = list('5 | .   .   .   .   .   .   .   .   . |')
    damier[11] = list('4 | .   .   .   .   .   .   .   .   . |')
    damier[13] = list('3 | .   .   .   .   .   .   .   .   . |')
    damier[15] = list('2 | .   .   .   .   .   .   .   .   . |')
    damier[17] = list('1 | .   .   .   .   .   .   .   .   . |')
    for i in range(2, 17, 2):
	    damier[i] = list('  |                                   |')
    position1 = dico['joueurs'][0]['pos']
    damier[position1[0]][position1[1]] = 1
    position2 = dico['joueurs'][1]['pos']
    damier[position2[0]][position2[1]] = 2
    horizontaux = dico["murs"]["horizontaux"]
    verticaux = dico["murs"]["verticaux"]
    for i in range(len(horizontaux)):
        j = 0
        while j<7 :
            damier[int((horizontaux[i][0])*3)][int((horizontaux[i][1])*4 + j)] = '-'
            j = j + 1
    
    liste = []
    for i in range(len(damier)):
	    liste.append(damier[i])
	    liste.append(['\n'])
    liste.pop()
    liste2 = [ item for elem in liste for item in elem]
    chaine = ''.join(liste2)
    print(chaine)
