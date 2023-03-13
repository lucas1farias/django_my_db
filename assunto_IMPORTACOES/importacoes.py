

def admin():
    """
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    """


def forms():
    """
    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.forms import UserChangeForm
    from django.core.mail.message import EmailMessage
    from django.utils.translation import gettext_lazy
    """


def _global():
    """
    from django.conf import settings
    from django.contrib.auth import get_user_model
    from django.urls import get_resolver
    """


def models():
    """
    from django.contrib.auth.models import AbstractBaseUser
    from django.contrib.auth.models import AbstractUser
    from django.contrib.auth.models import BaseUserManager
    from django.contrib.auth.models import User
    from django.contrib.auth.models import UserManager
    from django.db import models
    from django.db.models import signals
    from django.template.defaultfilters import slugify
    from django.utils.translation import gettext_lazy
    from model_mommy import mommy
    from stdimage import StdImageField
    """


def tests():
    """
    from django.test import TestCase
    from model_mommy import mommy
    """


def pp_urls():
    """
    from django.conf.urls.static import static
    from django.urls import include
    from django.urls import path
    """


def pa_urls():
    """
    from django.contrib.auth import views (aula 107) (36:50)
    from django.urls import path
    from django.urls import re_path (aula 88 / 04:55)
    """


# TODO: Programação Web com Python e Django framework: Essencial
def pa_utils():
    """
    Seção 11:Trabalhando com Geolocalização - 98. Criando um utilitário para IPs e busca - [ 01:15 ]
    from django.contrib.gis.geoip2 import GeoIP2
    from django.contrib.gis.geoip2 import geoip2
    """


def views():
    """
    from django.contrib import messages
    from django.contrib.auth.mixins import LoginRequiredMixin (aula 107) (32:55)
    from django.core.files.storage import FileSystemStorage (aula 105)
    from django.http import HttpResponse (aula 105)
    from django.http import FileResponse (aula 105)
    from django.http import JsonResponse
    from django.shortcuts import render
    from django.shortcuts import redirect
    from django.template.loader import render_to_string (aula 105)
    from django.urls import reverse_lazy
    from django.utils import translation
    from django.utils.safestring import mark_safe
    from django.utils.translation import gettext
    from django.views.generic import CreateView
    from django.views.generic import DeleteView
    from django.views.generic import FormView
    from django.views.generic import RedirectView
    from django.views.generic import TemplateView
    from django.views.generic import UpdateView
    from django.views.generic import View
    from django.views.generic.detail import DetailView
    from django.views.generic.list import ListView
    """


# TODO: Não vinculadas ao Django, mas usáveis em Python
def usar_com_django():
    """
    from textblob import TextBlob
    from pprint import pprint
    from uuid import uuid4
    """


# TODO: Importações não relacionadas com Python
def usar_em_python():
    """
    from chartjs.views.lines import BaseLineChartView (aula 101)
    from reportlab.pdfgen import canvas (aula 105)
    from weasyprint import HTML (aula 105)
    """


# TODO: Programação Web com Python e Django framework: Essencial
def consumers():
    """
    Curso  || Programação Web com Python e Django framework: Essencial
    Seção  || 10: Trabalhando com Aplicações em Tempo Real
    Aula   || 91. Criando o consumer
    Tempo  || 00:40 adiante

    from channels.generic.websocket import AsyncWebsocketConsumer
    """


def pp_routing():
    """
    from channels.auth import AuthMiddlewareStack   (Aula 88)
    from channels.routing import ProtocolTypeRouter (Aula 88)
    from channels.routing import URLRouter          (Aula 88)
    """


def outros():
    """
    # Importações Python usadas em projetos Django
        from textblob import TextBlob
        from pprint import pprint
        from uuid import uuid4

    # Importações não relacionadas com Python
        from chartjs.views.lines import BaseLineChartView (aula 101)
        from reportlab.pdfgen import canvas (aula 105)
        from weasyprint import HTML (aula 105)
    """
