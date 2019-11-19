import requests

idul = input('Saisir votre IDUL')

url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

def lister_parties(idul):
    rep = requests.get(url_base+'lister/', params={'idul': idul})
    game = []
    if rep.status_code == 200:
        game = game + rep.json()
    else:
        raise RuntimeError
    return game
    
def débuter_partie(idul):
    rep = requests.post(url_base+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        x = rep.json()
    else:
        raise RuntimeError
    return (x()['id'], x()['état'])

def jouer_coup(id_partie, type_coup, position):
    rep = requests.post(url_base+'jouer/', data={'id': id_partie, 'type':type_coup, 'pos':position})
    y = rep.json()
    if rep.status_code == 200:
        if 'gagnant' in y:
            return y['gagnant']
        else:
            return y['état']
    else:
        raise RuntimeError(y['message'])