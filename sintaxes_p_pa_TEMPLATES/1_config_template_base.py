

"""
* Em "nome da sua pasta dos templates", criar o template principal "main.html" ou "base.html"
* A sintaxe "{}" pertence ao Django e é aplicável em html (template)
* Todas as sintaxes {% block %} indicam que o template herdeiro têm permissão de inserir conteúdos independentes
* Tudo fora de {% block %} pertence ao template pai, tudo dentro, pertence ao template filho
* Esse template é passado p/ os próximos e evita repetição de códigos constantes

    ______________________________________________________ BASE ______________________________________________________
    <!DOCTYPE html>
    {% load static %}
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        {% block title %} {% endblock %}
        {% block css %} {% endblock %}
    </head>
    <body>
      {% block body %}

      {% endblock %}
    </body>
    </html>
"""
