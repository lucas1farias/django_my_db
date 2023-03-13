

def terminal():
    """

    """
    commands = {
        'python manage.py check',      # checar erros no projeto
        'python manage.py collectstatic',
        'python manage.py collectstatic - -clear',
        'python manage.py createsuperuser',
        'python manage.py inspectdb',  # não sei exatamente
        'python manage.py help',
        'python manage.py makemessages -l prefixo da língua'  # python manage.py makemessages -l ar en es fr ru zh-CN
        'python manage.py makemigrations',
        'python manage.py migrate',
        'python manage.py runserver',
        'python manage.py shell',
    }
