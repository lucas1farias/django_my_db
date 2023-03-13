

"""
Módulo: aula_106_seguranca.py
"""

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 12:Adicionando outras funcionalidades
    Aula:   # 106. Precisa melhorar a segurança da sua aplicação Django? Vamos lá!
    Minuto: #
    """

# Nesse projeto, aparentemente, não será necessário um [ pa ]
def terminal():
    """
    pip install django
    pip freeze > requirements.txt
    django-admin startproject pp .
    """

def settings():
    """
    from os import path
    ALLOWED_HOSTS = ['*']
    TEMPLATES = [{'DIRS': ['templates']}]
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'media')
    """

# Sobre seguranças contidas no framework Django
def obs():
    """
    1. Cross Site Scripting (XSS)
    2. Cross Site Request Forgery (CSRF) -> {% csrf_token %}
    3. SQL Injection
    4. Suporta HTTPS & TSL
    5. Armazenamento seguro de senhas, pelo algoritmo PBKDF2 com hash SHA256, recomendado pelo NIST
    """

# Conselho sobre segurança 1: Modificar rota administrativa
def pp_urls():
    """
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [path('zulassen', admin.site.urls)]
    """

# Conselho sobre segurança 1: Adicionar recursos de segurança extras ao módulo [ settings ]
def settings2():
    """
    SECURE_HSTS_SECONDS = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    X_FRAME_OPTIONS = 'DENY'
    # SECURE_SSL_REDIRECT = True
    """
    # SECURE_SSL_REDIRECT
    "Usado somente para modo produção, impede a aplicação de rodar em [ http ], apenas [ https ]"
    "Isso permite criptogração de dados entre cliente e servidor, aumentando a segurança"
    "Uma aplicação já em modo de desenvolvimento, não pode acessar o domínio via [ http ]"
    "Se o acesso for tentado via [ http ], haverá um redirecionamento para [ https ]"
