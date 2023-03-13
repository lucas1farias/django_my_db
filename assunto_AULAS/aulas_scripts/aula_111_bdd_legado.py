

"""
Módulo: aula_111_bdd_legado.py
"""

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 12:Adicionando outras funcionalidades
    Aula:   # 111. Usando banco de dados legado no seu projeto Django
    """

# Para demonstrar essa aula, é preciso a criação de dois projetos
"No projeto 1"
"1. configura-se o bdd em settings e cria-se ele no mysql workbench, para depois criar os modelos"
"No projeto 2"
"1. configura-se o bdd em settings"
"2. executam-se os comandos relacionados a legado"

# todo PROJETO 1

def terminal():
    """
    sudo apt-get install python3-dev default-libmysqlclient-dev -y
    pip install django==2.2.9
    pip install mysqlclient
    pip freeze > requirements.txt
    django.admin startproject pacote_proj .
    django.admin startapp pacote_app
    """

# Um bdd chamado: [ testar_legado ] será criado
def settings():
    """
    INSTALLED_APPS = ['pacote_app']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'testar_legado',
            'USER': 'luksadmin',
            'PASSWORD': 'passwort2772',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    """

def models():
    """
    from django.db import models

    class FullName(models.Model):
        full_name = models.CharField('Nome', max_length=100)

    class Nationality(models.Model):
        nationality = models.CharField('nacionalidade', max_length=100)

    class Age(models.Model):
        age = models.IntegerField('Idade')
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(FullName)
    class FullNameAdmin(admin.ModelAdmin):
        list_display = ('full_name',)

    @admin.register(Nationality)
    class NationalityAdmin(admin.ModelAdmin):
        list_display = ('nationality',)

    @admin.register(Age)
    class AgeAdmin(admin.ModelAdmin):
        list_display = ('age',)
    """

def mysql_workbench():
    """
    CREATE DATABASE testar_legado;
    Clicar no raio
    Clicar na seta a direita do nome SCHEMA (menu esquerdo da tela do MySQL Workbench)
    """

# O comando funciona quando há um bdd configurado corretamente no OS e nas configurações de um projeto Django
def terminal2():
    """ python manage.py inspectdb """

# todo PROJETO 2

def terminal3():
    """
    pip install django==2.2.9
    pip install mysqlclient
    pip freeze > requirements.txt
    django.admin startproject pp .
    django.admin startapp pa
    """

# Um bdd chamado: [ testar_legado ] já existente, é configurado no projeto nova (projeto 2)
"1. O django já vêm com um bdd sqlite3 configurado, e ele é diferente do bdd mysql"
"2. Se o comando abaixo, no terminal, for usado em um projeto com bdd sqlite3, não haverá tabelas a serem exibidas"
"3. Se o comando abaixo, no terminal, for usado em um projeto com bdd mysql, várias tabelas serão exibidas"
"4. Dentre as tabelas padrão exibidas, há também tabelas criadas nos projetos cujo esse bdd foi configurado"
"5. Nessa aula, por exemplo, um projeto chamado [ testar_legado ] foi criado, junto com 3 modelos/tabelas novos"
"6. Depois um segundo projeto, chamado [ legado ] foi criado, sem nenhum modelo"
"7. Porém, ambos projetos, possuem similaridades na sua configuração: receberam o mesmo bdd na var DATABASES"
"8. Sendo assim, as tabelas do projeto [ testar_legado ], tornam-se visíveis para o projeto [ legado ] também"
"9. A razão disso, é simplesmente por eles estarem ligados pelo mesmo banco de dados"
def settings2():
    """
    INSTALLED_APPS = ['pa']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'testar_legado',
            'USER': 'luksadmin',
            'PASSWORD': 'passwort2772',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    """

# Se def settings2 foi lido, o contexto continua aqui
"1. Esse projeto, que no contexto, chama-se [ legado ] têm o módulo [ models ] vazio"
"2. Se o comando 2 for executado, todas as tabelas exibidas no comando 1, serão copiadas para o módulo [ models ]"
"3. Se você usou o comando 1, presume-se que você queira a estrutura de outros bdds, para aplicar em um novo projeto"
"4. Se você usou o comando 2, presume-se que você queira passar a estrutura de outros bdds um novo projeto, sem edição"
"5. Ao executar o comando 2, nota-se em todos os modelos criados, a presença de uma classe Meta, [ managed = False ]"
"6. Isso significa que, os modelos agora existentes estão programados para não serem editáveis"
"7. Para editá-los, edite [ managed = True ] ou retire essa variável de todos os modelos"
# Desvantagens aparentes de modelos legado [ python manage.py inspectdb > pa/models.py ]
"8. O nome do modelo vêm com prefixos. Exemplo: legado = PacoteAppFullName / original = FullName"
"9. O rótulo (parâmetro 1 de criação de campo de um modelo) inserido no original, não vêm no legado"
# Incertezas que não foram testadas
"10. Criar modelo com Função __str__ em um projeto 1 e testar se o projeto 2 recebe-a como legado"
"11. Criar classe Meta: verbose_name, verbose_name_plural em um projeto 1 e testar se o projeto recebe-a como legado"
def terminal4():
    """
    python manage.py inspectdb
    python manage.py inspectdb > pa/models.py
    """

# Editando um dos modelos gerados pelo código acima
def models2():
    """
    class PacoteAppFullname(models.Model):
        full_name = models.CharField(max_length=100)

        def __str__(self):
            return self.full_name

        class Meta:
            managed = False
            db_table = 'pacote_app_fullname'
            verbose_name = 'Nome completo'
            verbose_name_plural = 'Nomes completos'
    """
    # Adicionados
    """
    def __str__(self):
            return self.full_name
            
    verbose_name = 'Nome completo'
    verbose_name_plural = 'Nomes completos'
    """

# No caso do registro, registram-se os modelos que você quer ver no template admin Django
"OBS: Deixar de registrar um modelo, não gera erro, mas ele não será exibido"
"OBS: Diferente do caso anterior, não há comando para facilitar o registro, apenas para passar modelos por legado"
def admin2():
    """
    from django.contrib import admin
    from .models import PacoteAppFullname

    @admin.register(PacoteAppFullname)
    class PacoteAppFullNameAdmin(admin.ModelAdmin):
        list_display = ('full_name',)
    """

def terminal5():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """
