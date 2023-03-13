

"""
Módulo >>> aula_87_para_92.py

Objetivo:
         criar um projeto Django de chat em tempo real
"""

# todo -> PARTE 1

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 10:Trabalhando com Aplicações em Tempo Real
    Aula:   # 87. Criando o projeto, a aplicação e configurando o Django Channels
    """

"OBS"  # De acordo com o professor, o bdd precisa ser o [ Redis ] pois ele é quem trabalha com o contexto: tempo real
def terminal():
    """
    pip install django=2.2.17 django-bootstrap4 django-channels channels-redis
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    from os import path

    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = ['bootstrap4', 'channels', 'pa', ]
    TEMPLATES = [{'DIRS': ['templates']}]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'staticfiles')
    STATIC_ROOT = path.join(BASE_DIR, 'media')

    ASGI_APPLICATION = 'pp.routing.application'
    CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6739)]
            }
        }
    }
    """

# todo -> PARTE 2

def fonte2():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 10:Trabalhando com Aplicações em Tempo Real
    Aula:   # 88. Configurando as Rotas e preparando para o WebSocket
    """
    # O que é um Websocket?
    "Iteração entre o cliente (browser) e uma aplicação web existente"

# Não existe, criar
def pa_urls():
    """
    from django.urls import *
    from .views import IndexTemplateView, RoomTemplateView

    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index'),
        path('bate-papo/<str:chat_room_name>', RoomTemplateView.as_view(), name='bate-papo')
    ]
    """
    # pa/new python file/urls

# Não existe, criar
def pa_routing():
    """
    from django.urls import re_path
    from .consumers import ChatConsumer

    websocket_urlpatterns = [
        re_path(r'ws/bate-papo/(?P<chat_room_name>\w+)/$', ChatConsumer)
        # re_path(r'ws/chat/(?P<nome_sala>\W+)/$')
    ]
    """
    # pa/new/python file/routing

def pp_urls():
    """
    from django.urls import include

    urlpatterns = [
        path('', include('pa.urls'))
    ]
    """

# Não existe, criar
def pp_routing():
    """
    from channels.auth import AuthMiddlewareStack
    from channels.routing import ProtocolTypeRouter
    from channels.routing import URLRouter
    from pa.routing import websocket_urlpatterns

    application = ProtocolTypeRouter(
        {'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpatterns),)}
    )
    """
    # pa/new/python file/routing

# todo -> PARTE 3

def fonte3():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 10:Trabalhando com Aplicações em Tempo Real
    Aula:   # 89. Trabalhando as Views
    """

def views():
    """
    import json
    from django.views.generic import TemplateView
    from django.utils.safestring import mark_safe

    class IndexTemplateView(TemplateView):
        template_name = 'index.html'

    class RoomTemplateView(TemplateView):
        template_name = 'bate-papo.html'

        def get_context_data(self, **kwargs):
            context = super(RoomTemplateView, self).get_context_data(**kwargs)
            context['chat_room_name_json'] = mark_safe(
                json.dumps(self.kwargs['chat_room_name'])
            )
            return context
    """

# todo -> PARTE 4

def fonte4():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 10:Trabalhando com Aplicações em Tempo Real
    Aula:   # 90. Criando os templates
    """

def templates():
    """ Template: index.html """
    # Construção entre: [ 01:22 até 12:27 ]
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página de bate-papo</title>
    </head>
    <body>
        <div class="container text-center mt-4">
            <h3 class="mb-4">Qual sala de bate-papo você deseja entrar?</h3>
            <label class="sr-only" for="chat_room_name">Campo para escrever o nome da sala de bate-papo</label>
            <input class="mb-4" id="chat_room_name" max="100" min="2" placeholder="Qual o nome da sala?" type="text">
            <button class="btn btn-success" id="this-btn">Entrar</button>
        </div>
    
        <script>
            document.querySelector('#chat_room_name').onkeyup = function(click){
                if(click.KeyCode == 13)
                {
                    document.querySelector('#this-btn').click();
                }
            };
    
            document.querySelector('#this-btn').onclick = function(click){
                var_chat_room_name = document.querySelector('#chat_room_name').value;
    
                if(chat_room_name != "")
                {
                    window.location.pathname = '/bate-papo/' + room_name + '/';
                }
                else
                {
                    alert('Você precisa informar o nome da sala!');
                    document.querySelector('#chat_room_name').focus();
                }
            };
        </script>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def templates2():
    """ Template: bate-papo.html """
    # Construção entre: [ 12:40 até 27:47 ]
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página de bate-papo</title>
    </head>
    <body>
        <div class="container text-center mb-2">
            <textarea id="room" cols="70" rows="20"></textarea>
            <label class="sr-only" for="chat_area">Campo para escrever sua mensagem</label>
            <input id="chat_area" size="100" type="text">
            <div class="container text-left mt-2"><button class="btn btn-success" id="this-btn">Enviar mensagem</button></div>
        </div>
    
        <script>
            var chat_room_name = {{ room_name_json }};
    
            var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + chat_room_name + '/');
    
            chatSocket.onmessage = function(click)
            {
                var stored_data = JSON.parse(click.data);
                var message = stored_data['message'];
                document.querySelector('#room').value += (message + '\n');
            };
    
            chatSocket.onclose = function(click)
            {
                console.error('O chat encerrou de forma inesperada!');
            };
    
            document.querySelector('#chat_area').focus();
    
            document.querySelector('#chat_area').onkeyup = function(click)
            {
                if(click.KeyCode == 13)
                {
                    document.querySelector('#this-btn').click();
                }
            };
    
            document.querySelector('#this-btn').onclick = function(click)
            {
                var messageInput = document.querySelector('#chat_area');
                var message = messageInput.value;
                chatSocket.send(JSON.stringify({'message': message;}));
                messageInput.value = '';
            };
        </script>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# todo -> PARTE 5

def fonte5():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 10:Trabalhando com Aplicações em Tempo Real
    Aula:   # 91. Criando o consumer
    """

# pa/new/python file/consumers
def pa_consumers():
    """
    from channels.generic.websocket import AsyncWebsocketConsumer
    import json

    class ChatConsumer(AsyncWebsocketConsumer):

        async def connect(self):
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'
            # Não foi explicado se f'chat' = nome do pa (no contexto do professor)

            await self.channel_layer.group.add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

        async def disconnect(self, code):
            await self.channel_layer.group.discard(
                self.room_group_name,
                self.channel_name
            )

        async def receive(self, text_data):
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            await self.channel_layer.group_send(
                self.room_group_name,
                {'type': 'chat_message', 'message': message}
            )

        async def chat_message(self, event):
            message = event['message']
            await self.send(text_data=json.dumps({'message': message}))
    """

# todo -> PARTE 6

def fonte6():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 10:Trabalhando com Aplicações em Tempo Real
    Aula:   # 92. Rodando nossa aplicação em Tempo Real
    """

def terminal3():
    """
    python manage.py migrate
    python manage.py runserver
    """
