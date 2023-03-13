

"""
* Formas de acessar o modelo Django padrão p/ usuários (p/ uso em algum contexto)

* Opções de criação de usuário:
    -> python manage.py createsuperuser
    -> Template admin
    -> Template com formulário que use request.POST['valor_atrib_name_do_input'] com os dados do modelo (Users)

* Opções de importação:
    -> from django.contrib.auth import get_user_model
    -> from django.contrib.auth.models import User

python manage.py shell
from django.contrib.auth import get_user_model
get_user_model()                                  -----> <class 'django.contrib.auth.models.User'>
get_user_model().objects.all()                    -----> <QuerySet [<User: lucasf>, <User: mario>, <User: Luigi>]>

get_user_model().objects.all()[0].is_superuser    -----> True
get_user_model().objects.all()[1].email           -----> 'mario@gmail.com'
get_user_model().objects.all()[2].username        -----> 'Luigi'

from django.contrib.auth.models import User
users = User.objects.all()
users                                             -----> <QuerySet [<User: lucasf>, <User: mario>, <User: Luigi>]>
"""
