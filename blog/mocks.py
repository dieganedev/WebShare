from django.http import Http404

class Poste():
    POSTES = [
        {'id': 1, 'name': 'prof1', 'tagline': 'professeur1', 'title': 'Chapitre1', 'file': 'Voici le premier chapitre'},
        {'id': 2, 'name': 'prof2', 'tagline': 'professeur2', 'title': 'Chapitre2', 'file': 'Voici le deuxiéme chapitre '},
        {'id': 3, 'name': 'prof3', 'tagline': 'professeur3', 'title': 'Chapitre3', 'file': 'Voici le troisiéme chapitre'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTES

    @classmethod
    def find(cls, id):
        try:
            return cls.POSTES[int(id) - 1]
        except:
            raise Http404('Désolé, poste #{} non trouvé.'.format(id))   

