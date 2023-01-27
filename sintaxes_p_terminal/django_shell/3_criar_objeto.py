

"""
* Para criar um objeto, é preciso um modelo criado, validado e migrado, p/ acessá-lo pelo Django Shell
* O modelo é importado ao shell p/ que seja possível a criação de um objeto via modelo
* Criar não é o suficiente, é preciso anexar esse objeto ao modelo
* O fato de o objeto referenciar um modelo, torna implícito que ao salvar, este é salvo p/ o modelo que o instancia

    python manage.py shell
    from _app.models import *
    new_noun = Nouns(name='dog', translation='cachorro')
    new_noun.save()
"""
