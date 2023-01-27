

"""
* O método "delete" funciona quando:
* Um objeto é acessado via índice [1], ou pelos métodos "get" [2] ou "filter" [3]


    python manage.py shell
    from _app.models import *
    nouns = Nouns.objects.all()
    new_noun = Nouns(name='dog', translation='cachorro')
    nouns     ----------> <QuerySet [<Nouns: dog>, <Nouns: dog>, <Nouns: dog>, <Nouns: goat>, <Nouns: cat>]>

    # [1] [2] [3]
    single_goat = nouns[7]
    single_cat = Nouns.objects.get(name='cat')
    multiple_dogs = Nouns.objects.filter(name='dog')

    single_goat.delete()
    single_cat.delete()
    multiple_dogs.delete()
"""
