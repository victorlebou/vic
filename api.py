import requests

IDUL = input('Saisir votre identifiant (IDUL)')

URL = 'https://python.gel.ulaval.ca/quoridor/api/'

def lister_parties(IDUL):
    """ Fait une liste de toutes les anciennes parties """
    rep = requests.get(URL+'lister/', params={'idul': IDUL})
    game = []
    if rep.status_code == 200:
        game = game + rep.json()
    else:
        raise RuntimeError
    return game
    
def débuter_partie(idul):
    """ permet de débuter la partie """
    rep = requests.post(URL+'débuter/', data={'idul': IDUL})
    try:
        if rep.json().get('message'):
            raise RuntimeError
        else:
            return rep.json()['id'], rep.json()['état']
    except RuntimeError:
        return rep.json()

def jouer_coup(id_partie, type_coup, position):
    """fonction qui exécute les coups des joueurs """
    rep = requests.post(URL+'jouer/', data={'id': id_partie, 'type':type_coup, 'pos':position})
    y = rep.json()
    try:
        if y.get('gagnant'):
            raise StopIteration
        elif y.get('message'):
            raise RuntimeError
        else:
            return rep.json()
    except StopIteration:
        return y
    except RuntimeError:
        return y