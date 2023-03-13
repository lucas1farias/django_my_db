

"""
Alterar partes específicas do template admin Django padrão
"""


def fonte():
    """
    Curso || Programação Web com Python e Django Framework: Essencial
    Aula  || 66. Extendendo o Django User Model
    Tempo || 37:40 adiante
    """


def terminal():
    """
    python manage.py shell
    from django.contrib import admin
    dir(admin.site)
    """


def pp_urls():
    """
    admin.site.site_header = 'Título da página de login do Django template admin'
    admin.site.site_title  = <title></title>
    admin.site.index_title = <h1></h1>

    ALTERNATIVO
        from django.contrib.auth.models import User
        admin.site.site_title = f'Bem-vindo, admin {User.objects.get(username="Lucas").get_full_name()}'
    """
