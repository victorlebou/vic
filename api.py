import argparse
parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
parser.add_argument('-l', '--lister', metavar='',help="Lister les identifiants de vos 20 dernières parties")
parser.add_argument('identification', nargs='+', metavar= 'idul', help='IDUL du joueur')
parser.parse_args()