

"""
Módulo: migrations.py
Objetivo: deletar migrações de forma segura, evitando gerar bugs no projeto, caso haja remoção manual
Palavra chave: corrigir migrations
"""


def remover_dir_migrations_forma_recomendada():
    """
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
    corrigir possíveis erros
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    """
