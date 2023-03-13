

"""
* Pelo método "filter", o objeto é capturado e acessado por indexação seguida de notação ponto
* Ele serve p/ coletar MÚLTIPLOS OBJETOS, portanto, é apropriado p/ consultas caso modelos tenham objetos repetidos

    python manage.py shell
    from _app.models import *
    nouns = Nouns.objects.all()
    new_noun = Nouns(name='dog', translation='cachorro')
    new_noun.save()
    nouns                               ----------> <QuerySet [<Nouns: dog>]>
    new_noun2 = Nouns(name='dog', translation='cachorro')
    new_noun.save()
    nouns                               ----------> <QuerySet [<Nouns: dog>]>
    dog_obj_filtered = Nouns.objects.filter(name='dog')
    dog_obj_filtered                    ----------> <QuerySet [<Nouns: dog>, <Nouns: dog>]>
    dog_obj_filtered[0].name            ----------> 'dog'
    dog_obj_filtered[1].translation     ----------> 'cachorro'
    dog_obj_filtered.first()            ----------> <Nouns: dog>
    dog_obj_filtered.last()             ----------> <Nouns: dog>
    dog_obj_filtered.first().name       ----------> 'dog'
    dog_obj_filtered.last().translation ----------> 'cachorro'
"""
