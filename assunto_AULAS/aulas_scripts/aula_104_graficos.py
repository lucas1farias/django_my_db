

"""
Módulo: aula_104_graficos.py
"""

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 12:Adicionando outras funcionalidades
    Aula:   # 104. Precisa gerar gráficos na sua aplicação Django? Valos lá!
    """

def browser():
    """
    Pesquisa  # chart.js
    Website   # https://www.chartjs.org/
    Conceito  # biblioteca gratuita para usar gráficos em projetos/templates
    """

def terminal():
    """
    pip install django
    pip install django-bootstrap4
    pip install django-chartjs
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    from os import path
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = ['pa', 'bootstrap4', 'chartjs']
    TEMPLATES = [{'DIRS': ['templates']}]
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'media')
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

# Não existe, criar: [ raiz/pa/new/python file/urls ]
def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index'),
        path('dados/', DadosJsonTemplateView.as_view(), name='dados'),
    ]
    """

# Não existe, criar: [ raiz/pa/new/directory/templates ] [ raiz/pa/templates/new/html file/index ]
def templates_index():
    """
    <!doctype html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
      <head>
        {% bootstrap_css %}
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Índice</title>
      </head>
      <body>
        <div class="container text-center mt-2 mb-2">
          <h2 class="text-success">Página Índice</h2>
        </div>

        <div class="container text-center mt-2 mb-2">
            <canvas id="grafico" height="400" width="500"></canvas> <!-- var ctx -->
        </div>

      {% bootstrap_javascript jquery='full' %}
      <script src="{% static 'js/Chart.min.js' %}" type="text/javascript"></script>
      <script type="text/javascript">
        $.get('{% url "dados" %}', function(data)
        {
          var ctx = $("#grafico").get(0).getContext("2d");
          new Chart(ctx, {type: 'line', data: data});
        });
      </script>
      </body>
    </html>
    """

def views():
    """"""
    '''
    from random import randint
    from chartjs.views.lines import BaseLineChartView
    from django.views.generic import TemplateView
    
    class IndexTemplateView(TemplateView):
        template_name = 'index.html'
    
    class DadosJsonTemplateView(BaseLineChartView):
    
        # Função de nome mandatório
        # Colunas
        def get_labels(self):
            """ Retornar 12 labels para o eixo x do gráfico """
            labels = [
                'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
            ]
            return labels
    
        # Função de nome mandatório
        # Linhas
        def get_providers(self):
            """ Retornar o nome dos datasets """
            datasets = [
                'Curso hacker iniciante Python',
                'Curso HTML5 e CSS4',
                'Curso de Banco de dados Relacionais',
                'Curso de Programação para Leigos',
                'Curso de Linguagem de programação Python',
                'Curso de Linguagem de programação C',
            ]
            return datasets
    
        # Função de nome mandatório
        def get_data(self):
            """
            1. Retornar 6 datasets para plotar o gráfico
            2. Cada linha contêm 1 dataset
            3. Cada linha contêm 1 label
            4. Quantidade de dados == labels & datasets [ mandatório ]
            """
            dados = []
            for linhas in range(6):
                for colunas in range(1):
                    add = [randint(1, 200), randint(1, 200), randint(1, 200), randint(1, 200),
                           randint(1, 200), randint(1, 200), randint(1, 200), randint(1, 200),
                           randint(1, 200), randint(1, 200), randint(1, 200), randint(1, 200)]
                    dados.append(add)
            return dados
    '''

def terminal2():
    """
    python manage.py migrate
    python manage.py runserver
    """
