

"""
* A var de classe "context_object_name" faz o mesmo papel de instanciar uma var de contexto em "get_context_data"
* A var de classe "context_object_name" é usada majoritariamente p/ apresentar os objetos de um modelo
* A var de classe "model" diz a view qual o modelo a ser apresentado
* Pela var de classe "context_object_name" é preciso fazer coisas, como:
    {% if user_tasks|length == 0 %} {% endif %}
    {% for task in user_tasks %} {% endfor %}
* Além do objeto de contexto, nesse tipo de view é apropriado as vars de classe "ordering" e "paginate_by"
* Elas ajudam na configuração de templates ligados a essa view, SE no template há paginação incluída

from django.views.generic import ListView
from .models import *

class UserTasks(ListView):
    template_name = 'user_tasks.html'
    context_object_name = 'user_tasks'  # nome da var de contexto
    model = Tasks

    # Paginação
    ordering = 'created'  # ordenar via atributo
    paginate_by = 5       # exibir 5 itens por linha (quebra p/ segunda página)
"""
