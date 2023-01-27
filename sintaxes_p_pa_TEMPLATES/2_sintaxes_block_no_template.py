

"""
* No exemplo abaixo, temos 3 {% block %}, isso significa:
* O conteúdo fora dos "blocks" pode ser copiado p/ outro template, se ele for o provedor
* O conteúdo dentro dos "blocks" é independente, onde o template herdeiro anexa o que for desejado
* Basicamente, se um template herdeiro recebe o exemplo, ele terá tags "title", "link", "body" próprias
* O template herdeiro precisa chamar os mesmos block dentro de si, com seus próprios conteúdos

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
