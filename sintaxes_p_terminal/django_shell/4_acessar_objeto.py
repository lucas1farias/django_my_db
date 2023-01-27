

"""
* Os objetos são do tipo "QuerySet" e seu acesso se dá via: índice
* Para obter os dados do objeto descriptagrafados, além do índice, se aplica: notação ponto do atrib.

    python manage.py shell
    from _app.models import *
    nouns = Nouns.objects.all()
    new_noun = Nouns(name='dog', translation='cachorro')
    nouns                ----------> <QuerySet [<Nouns: dog>]>
    len(nouns)           ----------> 1
    nouns[0]             ----------> <Nouns: dog>
    nouns[0].name        ----------> 'dog'
    nouns[0].translation ----------> 'cachorro'
"""
