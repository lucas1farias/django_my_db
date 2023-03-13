

"""
Módulo: aula_110_admin_mais_completo.py
"""

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 12:Adicionando outras funcionalidades
    Aula:   # 110. Customizando, ainda mais, o admin do Django
    """

# todo CONFIGURAÇÃO BÁSICA

def browser():
    """ http://127.0.0.1:8000/admin/ """
    # Se estiver logado, deslogar, para vizualizar a página inicial de login

def pp_urls():
    """
    1. admin.AdminSite.site_header = ''  # título de apresentação de login do template admin Django
    2. admin.site.site_header = ''       # título de apresentação de login do template admin Django
    3. admin.AdminSite.site_title = ""   # tag <title></title> do template admin Django
    4. admin.site.site_title = ""        # tag <title></title> do template admin Django
    5. admin.AdminSite.index_title = ''  # tag <h1></h1> do template admin Django, na tela de entrada após login
    6. admin.site.index_title = ''       # tag <h1></h1> do template admin Django, na tela de entrada após login
    """
    # 1. python manage.py shell -> from django.contrib import admin -> dir(admin.AdminSite)
    # 2. python manage.py shell -> from django.contrib import admin -> dir(admin.site)
    # 3. python manage.py shell -> from django.contrib import admin -> dir(admin.AdminSite)
    # 4. python manage.py shell -> from django.contrib import admin -> dir(admin.site)
    # 5. python manage.py shell -> from django.contrib import admin -> dir(admin.AdminSite)
    # 6. python manage.py shell -> from django.contrib import admin -> dir(admin.site)

# todo INSTALAÇÃO ADMINLTE2

def terminal():
    """ pip install django-adminlte2 """

def settings():
    """ INSTALLED_APPS = ['django_adminlte', 'django_adminlte_theme'] """

# todo CONFIGURAÇÃO AVANÇADA - EDITAR TEMPLATE ADMIN PADRÃO

"/home/lucas/.virtualenvs/slugify/lib/python3.8/site-packages/django/contrib/admin/templates"
"1. Abrir o diretório [ templates ], copiar o diretório [ admin ]"

# No projeto, cria-se um diretório [ templates ] e dentro deste, cola-se o diretório [ admin ]
def projeto():
    """ raiz/new/directory/templates """
    # você então passa a ter acesso aos templates admin, de dentro do projeto

# todo CONFIGURAÇÃO AVANÇADA - EDITAR TEMPLATE ADMIN LTE2

"/home/lucas/.virtualenvs/slugify/lib/python3.8/site-packages"
"1. Abrir o diretório [ site-packages ], seguido de [ django_adminlte ] e [ templates ], copiar [ adminlte ]"
"2. Abrir o diretório [ site-packages ], seguido de [ django_adminlte_theme ] e [ templates ], copiar [ admin ]"

# No projeto, cria-se um diretório [ templates ] e dentro deste, cola-se os diretório [ adminlte ] e [ admin ]
def projeto2():
    """ raiz/new/directory/templates """
    # você então passa a ter acesso aos templates adminlte2, de dentro do projeto

# templates/admin/base_login.html
def template():
    """ <p class="login-box-msg"></p> """

# templates/admin/login.html
def template2():
    """
    1. <input type="text" id="id_username" name="username" class="form-control" placeholder="seu usuário">
    2. <input type="password" id="id_password" name="password" class="form-control" placeholder="sua senha">
    3. <button class="btn btn-primary btn-block btn-flat" type="submit">{% trans 'entrar' %}</button>
    """
    # 1 e 2. modificando placeholder
    # 3. modificando botão de acesso

# templates/adminlte2/lib/_main_header.html
def template3():
    """
    <span class="logo-mini">{% block logo_text_small %}<b>App</b>{% endblock %}</span>
    <span class="logo-lg">{% block logo_text %}<b>Aplicativo</b>{% endblock %}</span>
    """
    # 1 e 2. Modificando nomes de navegação na tela pós login
