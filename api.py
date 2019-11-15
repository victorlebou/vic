import requests

url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

def lister_parties(identifiant):
    rep = requests.get(url_base+'lister/', params={'idul': 'identifiant'})
    if rep.status_code == 200:
        parties = rep.json()
    else:
        raise RuntimeError
    return parties
    
def débuter_partie(identifiant):
    rep = requests.post(url_base+'débuter/', data={'idul': 'identifiant'})
    if rep.status_code == 200:
        idetat = rep.json()
    else:
        raise RuntimeError
    return (idetat()['id'], idetat()['état'])

if __name__ == "__main__":
    print(débuter_partie(''))