

"""
* Pelo método "get", o objeto é capturado e acessado por notação ponto
* Ele só coleta UM OBJETO, portanto, se numa consulta há objetos repetidos, haverá erro (ao invés: usar filter)

    python manage.py shell
    from _app.models import *
    nouns = Nouns.objects.all()
    new_noun = Nouns(name='dog', translation='cachorro')
    nouns                      ----------> <QuerySet [<Nouns: dog>]>
    dog_obj_gotten = Nouns.objects.get(name='dog')
    dog_obj_gotten             ----------> <Nouns: dog>
    dog_obj_gotten.name        ----------> 'dog'
    dog_obj_gotten.translation ----------> 'cachorro'
"""
