

"""
* O exemplo uso um objeto único (objects.get) que necessita somente a notação ponto
* Após editar com a reatribuição, o comando "save()" valida a alteração, e depois é mostrada a diferença
* Se fossem objetos múltiplos (objects.filter), a reatribuição deve ter indexação antes da notação ponto

    python manage.py shell
    from _app.models import *
    db = Nouns.objects.all()
    this_obj = Nouns.objects.get(name='dog')

    this_obj.name        ----------> 'dog'
    this_obj.translation ----------> 'cachorro'

    this_obj.translation = 'gato'
    this_obj.save()

    this_obj.name        ----------> 'dog'
    this_obj.translation ----------> 'gato'
"""
