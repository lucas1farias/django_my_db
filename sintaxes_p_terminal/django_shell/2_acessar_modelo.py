

"""
* Para acessar um modelo, este deve ter sido criado, validado e configurado seus módulos de migração
* Todo modelo Django é um "QuerySet"

python manage.py shell
from _app.models import *
nouns = Nouns.objects.all()
nouns          ----------> <QuerySet []>
type(nouns)    ----------> <class 'django.db.models.query.QuerySet'>
"""
