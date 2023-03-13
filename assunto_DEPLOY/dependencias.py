

"""
A - servidor do modo produção para Django, substituindo o modo desenvolvimento: [ python manage.py runserver ]
B - servir módulos estáticos enquanto o projeto estiver em modo produção [ DEBUG = False ]
    melhoria de: [ python manage.py collectstatic ]

pip install gunicorn (A)
pip install whitenoise (B)
"""
