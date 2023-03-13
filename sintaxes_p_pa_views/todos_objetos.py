

"""
* Diferenças entre modelo com seus objetos em formato comum e JSON

def __init__(self, **kwargs):
    super().__init__(**kwargs)

    # OUTROS COMANDOS TALVEZ ÚTEIS
    self.db_length = Language.objects.count()
    self.first_obj = Language.objects.first()
    self.last_obj =  Language.objects.last()

    self.db = Language.objects.all()
    self.db_json = Language.objects.all().values()

______________________________________________________ DIFERENÇAS ______________________________________________________

self.db = <QuerySet [
    <Language: Python>, <Language: Javascript>, <Language: Ruby>, <Language: Assembly>, <Language: C++>,
    <Language: Python>
]>

self.db_dict = <QuerySet [
    {'id': 20, 'name': 'Python'}, {'id': 21, 'name': 'Javascript'}, {'id': 22, 'name': 'Ruby'},
    {'id': 23, 'name': 'Assembly'}, {'id': 24, 'name': 'C++'}, {'id': 25, 'name': 'Python'}
]>

self.db[0]      = <Language: Python>
self.db_dict[0] = {'id': 20, 'name': 'Python'}

self.db.filter(name="Python")      = <QuerySet [<Language: Python>, <Language: Python>]>
self.db_dict.filter(name="Python") = <QuerySet [{'id': 20, 'name': 'Python'}, {'id': 25, 'name': 'Python'}]>

self.db.filter(name="Python")[0]      = <Language: Python>
self.db_dict.filter(name="Python")[0] = {'id': 20, 'name': 'Python'}

self.db.filter(name="Python")[0].name         = 'Python'
self.db_dict.filter(name="Python")[0]["name"] = 'Python'
"""
