

"""
Módulo: aula_107_login_facebook.py
"""

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 12:Adicionando outras funcionalidades
    Aula:   # 107. Precisa fazer login com Facebook na sua aplicação? Vamos lá!
    """

# Para mais informações sobre o social auth, e como inserir outras autenticações por mídia social, pesquisar:
"python social auth documentation -> backends -> social backends"
def terminal():
    """
    pip install django
    pip install django-bootstrap4
    pip install social-auth-app-django
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

# A autenticação com login em mídias sociais acontece aqui, pela var [ AUTHENTICATION_BACKENDS ]
"O django possui uma forma de autenticação padrão = [ django.contrib.auth.backends.ModelBackend ]"
"Se a autenticação for somente por mídia social, o padrão do Django deve estar ausente"
def settings():
    """
    from os import path
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = ['pa', 'bootstrap4', 'social_django']
    TEMPLATES = [{'DIRS': ['templates']}]

    TEMPLATES = [
        'context_processors':[
            'social_django.context_processors.backends',
            'social_django.context_processors.login_redirect'
        ]
    ]

    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'media')
    """
    # social_django.context_processors.backends
    "dar acesso para o social_django, aos campos de autenticação adquiridos nos templates"

    # social_django.context_processors.login_redirect
    "dar acesso para a social_django, aos campos de autenticação adquiridos nos templates"

# A variável TEMPLATES foi alterada, com isso, torna-se necessário a aplicação de migração
def terminal2():
    """ python manage.py migrate """

# base.html
def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
    </head>
    <body>
        <div class="container-fluid text-center">
            <div>
                <h1 class="text-primary">{% block title %}{% endblock %}</h1>
                <div class="card p-5">
                    {% block content %}{% endblock %}
                </div>
            </div>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# login.html
def templates2():
    """
    {% extends 'base.html' %}
    {% block title %}Página de login{% endblock %}
    {% block content %}
        <div class="row">
            <div class="col-md-8 mx-auto social-container my-2 order-md-1">
                <a class="btn btn-dark text-danger mb-2" href="#" role="button">Login com Facebook</a>
            </div>
        </div>
    {% endblock %}
    """
    # <a class="btn btn-dark text-danger mb-2" href="#" role="button">Login com Facebook</a>
    "no contexto, foi usado o facebook, copie e cole, mudando o título, para adicionar outras mídias sociais"

# index.html
def templates3():
    """
    {% extends 'base.html' %}
    {% block title %}Página Inicial{% endblock %}
    {% block content %}
        <div class="row">
            <div class="col-sm-12 mb-3">
                <h2 class="text-center">Bem-vindo(a), {{ user.username }}</h2>
            </div>
        </div>
    {% endblock %}
    """

def styles():
    """
    img {border: #282c34;}

    .container-fluid {
        align-items: center;
        background-color: #282c34;
        display: flex;
        height: 100vh;
        justify-content: center;
    }

    .container-fluid > div {
        max-width: 500px;
        min-width: 300px;
        width: 85%;
    }

    .card {width: 100%;}

    .social-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .btn a, .btn a:hover {color: white; text-decoration: none;}
    """

def views():
    """
    from django.views.generic import TemplateView
    from django.contrib.auth.mixins import LoginRequiredMixin

    # Lembrando que aqui há um mixin, e ele sempre vêm à esquerda na herança
    class IndexTemplateView(LoginRequiredMixin, TemplateView):
        template_name = 'index.html'

    class LoginTemplateView(TemplateView):
        template_name = 'login.html'
    """

def pp_urls():
    """
    from django.urls import include

    urlpatterns = [path('', include('pa.urls'))]
    """

# A última rota autentica o social_django, sendo assim, é mandatória
def pa_urls():
    """
    from django.urls import include, path
    from django.contrib.auth import views as auth_views
    from .views import *

    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index'),
        path('login/', LoginTemplateView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('social-auth/', include('social_django.urls', namespace='social'))
    ]
    """

def settings2():
    """
    LOGIN_URL = 'login'             # quando estiver deslogado, redirecionar para essa rota
    LOGIN_REDIRECT_URL = 'index'    # quando efetuar login, redirecionar para essa rota
    LOGOUT_REDIRECT_URL = 'logout'  # quando efetuar logout, redirecionar para essa rota (ver pa_urls)
    LOGOUT_URL = 'login'            # quando estiver deslogado, redirecionar para essa rota
    """

# É mandatório ter uma conta no facebook, para conseguir acessar
"Menu  [ como começar ] [ criar experiências conectadas ]"
"Campo [ nome de exibição do aplicativo ] = nome do av (foi recomendado)"
"Menu  [ configurações/básico ]"
"Campo [ domínios do aplicativo ], inserir [ localhost ou a rota de uma aplicação já criada/deploiada ]"
"Botão [ adicionar plataforma ] [ site ] [ url do site ] = inserir [ http://localhost:8000/ ]"
# Se a aplicação já foi deploiada...
"Clicar em [ adicionar plataforma ] [ site ] [ url do site ] = nome da rota dopliada"
def browser():
    """ https://developers.facebook.com/apps """

def settings3():
    """
    # Configurações para qualquer mídia social (uma vez feito login por uma mídia, não precisa ser refeito)
    SOCIAL_AUTH_RAISE_EXCEPTIONS = False

    # Configurações para facebook
    SOCIAL_AUTH_FACEBOOK_KEY = '777345242996696'                      # Configurações [ ID do aplicativo ]
    SOCIAL_AUTH_FACEBOOK_SECRET = 'ec799c51a7edac27f52842155b1290cd'  # Configurações [ Chave Secreta do Aplicativo ]
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']
    SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id, name, email, picture.type(large), link'}
    SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [('name', 'name'), ('email', 'email'), ('picture', 'picture'), ('link', 'profile_url')]
    """

# login.html
def templates4():
    """ href="{% url 'social:begin' 'facebook' %}" """
    # Após as configurações feitas, o atributo [ href="#" ] precisa ser modificado

# index.html
def templates5():
    """
    {% for each_data in backends.associated %}
        {% if each_data.provider == 'facebook' %}
            <div class="col-md-4 text-center">
                <img
                    alt="Imagem do usuário logado"
                    height="130"
                    src="{{ each_data.extra_data.picture.data.url }}"
                    style="border-radius: 50%;"
                    width="130"
                >
            </div>
            <div class="col-md-8 social-container my-2">
                <p>Logado via: {{ each_data.provider }}</p>
                <p>Nome: {{ each_data.extra_data.name }}</p>
                <p>Perfil: <a href="{{ each_data.extra_data.profile_url }}" >acessar</a></p>
            </div>
        {% endif %}
    {% endfor %}
    <div class="col-sm-12 mt-2 text-center">
        <a class="btn btn-primary text-dark" href="{% url 'logout' %}">encerrar/logout</a>
    </div>
    """
    # A configuração feita acima, só é possível pela instalação feita na variável TEMPLATES
    "social_django.context_processors.backends"

def problemas():
    """
    1. O site apresentou problemas de segurança e não foi possível fazer login pelo facebook
    2. Foi recomendável fazer o deploy [ heroku ] [ git_heroku_deploy ]
    3. A aplicação foi deploiada, e as configurações modificadas em [ https://developers.facebook.com/apps/ ]
    4. Mesmo com as mudanças, o problema de segurança para logar no facebook persiste
    5. vai tomar no cu...
    """

def se_sucesso():
    """
    python manage.py createsuperuser
    python manage.py runserver
    """
    # Aparentemente, ao fazer login, cria-se um novo objeto ao bdd [ Users ], padrão do Django
