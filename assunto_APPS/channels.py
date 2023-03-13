

def fonte():
    """
    Curso    || Programação Web com Python e Django Framework: Essencial
    Seção    || 10: Trabalhando com Aplicações em Tempo Real
    Aula     || 87. Criando o projeto, a aplicação e configurando o Django Channels
    Objetivo || Aplicação que faz o Django trabalhar em "real time" com um bdd Redis (projeto de chat)
    """


def instalacao():
    """
    * Aplicação e seu banco de dados que a integra

    pip install django-channels
    pip install channels-redis
    """


def settings():
    """
    * Na aula, foi posicionado no índice inicial, mas é preferido ao fundo
    * A var (ASGI_APPLICATION) é uma configuração específica p/ o (channels)
    * Django normalmente suporta aplicações do tipo (WSGI), mas essa aplicação é do tipo (ASGI), por isso essa config.

    INSTALLED_APPS = ['channels']
    ASGI_APPLICATION = 'nome_projeto.routing.application'

    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.app.RedisChannelLayer',
            'CONFIG': {
                'hosts': [('127.0.0.1', 6379)]
            },
        },
    }
    """


def urls():
    """
    * 2 urls p/ 2 views

    from .views import *
    path('', Chat.as_view(), name='chat'),
    path('chat/<str:name-room>/', Room.as_view(), name='room'),
    """


def pa_routing():
    """
    * Criar na raiz do pacote aplicação (routing.py)

    from django.urls import re_path
    from .consumers import ChatConsumer

    websocket_urlpatterns = [
        re_path(r'ws/chat/(?P<name-room>\w+)/$', ChatConsumer)
    ]
    """


def pp_routing():
    """
    * Criar na raiz do pacote projeto (routing.py)

    from channels.routing import ProtocolTypeRouter, URLRouter
    from channels.auth import AuthMiddlewareStack
    from app.routing import websocket_urlpatterns

    application = ProtocolTypeRouter(
        {
            'websocket': AuthMiddlewareStack(
                URLRouter(
                    websocket_urlpatterns
                )
            ),
        }
    )
    """
