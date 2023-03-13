

"""
* No Django, todo modelo é um QuerySet, sua conversão p/ formato JSON se dá pela função ".values()"

python manage.py shell
from pa.models import *
db = Language.objects.all().values()
db

<QuerySet [
    {'id': 20, 'name': 'Python'},
    {'id': 21, 'name': 'Javascript'},
    {'id': 22, 'name': 'Ruby'},
    {'id': 23, 'name': 'Assembly'}
]>

db[0]    ----------> {'id': 20, 'name': 'Python'}
db[1]    ----------> {'id': 21, 'name': 'Javascript'}
"""
