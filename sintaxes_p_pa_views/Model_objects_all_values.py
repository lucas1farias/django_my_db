

"""
* Exibir objetos de um modelo numa view, de forma que eles se apresentem em forma de JSON
* Sintaxe alterada || Model.objects.all().values()
* Instanciação preferencialmente no método __init__ ou no método "get_context_data"

def get_context_data(self, **kwargs):
    context = super(View, self).get_context_data(**kwargs)
    context['model_json'] = Model.objects.all().values()
    return context

* EXEMPLO:
    <QuerySet [
        {'id': 20, 'name': 'Python'}, {'id': 21, 'name': 'Javascript'},
        {'id': 22, 'name': 'Ruby'},
        {'id': 23, 'name': 'Assembly'}
    ]>
"""


def exemplo_django_shell():
    """
    python manage.py shell
    from pa.models import *
    q = Interview.objects.all().values()
    q

        <QuerySet [
            {'id': 10, 'full_name': 'Pessoa2', 'email': 'pessoa2@gmail.com', 'age': 21, 'gender': 'masculino',
             'nationality': 'Brasileiro', 'brief_description': 'Eu gosto da cor amarela', 'self_grade': Decimal('8.0'),
              'passtimes': 'Pular corda', 'slug': 'pessoa2', 'avatar': 'database_interview/scorpion.png'},
            {'id': 9, 'full_name': 'Pessoa1', 'email': 'pessoa1@gmail.com', 'age': 25, 'gender': 'feminino',
             'nationality': 'Brasileiro', 'brief_description': 'Eu faço bolo de milho', 'self_grade': Decimal('6.9'),
             'passtimes': 'Cantar', 'slug': 'pessoa1', 'avatar': 'database_interview/IMG-20201211-WA0002_1.jpg'}
        ]>

    q[0]['id']        >>> 10
    q[0]['full_name'] >>> 'Pessoa2'
    q[1]['email']     >>> 'pessoa1@gmail.com'
    q[1]['age']       >>> 25
    """
