

"""
REQUISITOS:
  * Um modelo criado, configurado, validado e migrado
  * Dados externos que servirão como objetos (um módulo '.py' que tenha um+ iterável repr. cada atrib.)
  * Exemplo:
      -> Módulo: new_objects.py
      -> Conteúdo:
          nouns = ['dog', 'cat', 'mouse']
          nouns_pt_br = ['cachorro', 'gato', 'rato']

  * O loop em si já acessa os índices do atributo "name", enquanto a var interna "i" acessa "translation"
  * Poderia ser feito um loop com range, mas foi optado o recurso acima (acredito que consome menos)
  * Dependendo da qtd. de objetos criados, esse procedimento pode demorar

    python manage.py shell
    from _app.models import Nouns
    from new_objects import *
    for i, index in enumerate(nouns):
        atrib_name = index
        atrib_translation = nouns_pt_br[i]
        new_obj = Nouns(name=atrib_name, translation=atrib_translation)
        new_obj.save()
"""
