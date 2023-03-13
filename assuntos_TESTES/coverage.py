

"""
Módulo:
"""

"------------------------------------------------------ ETAPA 1 ------------------------------------------------------"

# criar uma pasta, abri-la numa IDE, criar um ambiente virtual

"----------------------------------------------- CONFIGURAÇÕES INICIAIS -----------------------------------------------"

def terminal():
    """
    pip install django==2.2.17
    pip install django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = 'DIRS': ['templates']
    """

# Criação de um modelo genérico, para exemplificar o uso do [ Coverage ]
def models():
    """
    from django.db import models

    class Modelo(models.Model):
        texto = models.CharField('Texto', max_length=500)

        class Meta:
            verbose_name = 'Texto'
            verbose_name_plural = 'Textos'

        def __str__(self):
            return self.texto
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(Modelo)
    class ModeloAdmin(admin.ModelAdmin):
        list_display = ('texto',)
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    """


"----------------------------------------- CONFIGURANDO O AMBIENTE DE TESTES -----------------------------------------"

""  # raiz / new / python package / tests
""  # tests / new / python file / test_models
""  # tests / new / python file / test_forms
""  # tests / new / python file / test_views

"--------------------------------------- INSTALAÇÃO DE DEPENDÊNCIAS PARA TESTES ---------------------------------------"


def terminal3():
    """
    pip install model_mommy
    pip install coverage
    pip freeze > requirements.txt
    """


"---------------------------------------- ARQUIVO DE CONFIGURAÇÃO DO COVERAGE ----------------------------------------"

""     # raiz / new / file / .coveragerc
"OBS"  # após todos os testes passarem, é uma boa ideia adicionar a esse módulo: [ htmlcov/* ]


def configurar_arquivo_coveragerc():
    """
    [run]
    source = .

    omit =
        */__init__.py
        */settings.py
        */manage.py
        */wsgi.py
        */apps.py
        */urls.py
        */admin.py
        */migrations/*
        */tests/*
    """


"---------------------------------------------- IGNORAR ARQUIVO COVERAGE ----------------------------------------------"

# htmlcov/*

"---------------------------------------- COMANDO PARA REALIZAR TESTE COVERAGE ----------------------------------------"
""  # Aparentemente, ao executar esse comando, é procurado no projeto, arquivos com prefixo [ test ]


def terminal4():
    """ coverage run manage.py test """


"----------------------------------------- COMANDOS RELACIONADOS AO COVERAGE -----------------------------------------"
""  # O comando 1 exibe um relatório do progresso dos testes, com os módulos filtrados, via terminal
""  # O comando 1 serve para acompanhar o progresso dos testes via terminal (consulta rápida)
""  # O comando 2 cria um diretório do progresso dos testes, para vê-los em um servidor local (consulta analítica)
""  # O comando 3 dá acesso ao servidor local de testes
""  # O comando 4 deleta o diretório de testes (normalmente usado após ter progresso nos testes)
""  # Os comandos 2, 3 e 4 são normalmente feitos em conjunto
""  # 2 gera a consulta, 3 mostra o que ainda deve ser corrigido, 4


def comandos_coverage():
    """
    coverage report        (consulta rápida)
    coverage html          (consulta analítica)
    python -m http.server  (acesso à consulta analítica)
    rm -rf htmlcov         (remoção de banco de dados)
    """


def ordem_comum():
    """
    - Cria-se um teste (exemplo está no tópico abaixo deste)

    - Executa-se o teste:
        coverage run manage.py test

    - Se o teste falha:
        - será preciso investigar o erro
        - se já não tiver criado o banco de dados, fazer [ coverage html               ]
        - acessa-se o banco de dados                     [ python -m http.server       ]
        - tenta-se corrigir o erro
        - testa-se novamente pra ver se passa            [ coverage run manage.py test ]

    - Se o teste passa:
        - verifica-se o progresso por                  [ coverage report ]
        - remove-se o banco de dados desatualizado por [ rm -rf htmlcov  ]
        - cria-se um banco de dados atualizado por     [ coverage html   ]
    """

"----------------------------- EXEMPLO DE TESTE DE MODELOS: raiz / tests / test_models.py -----------------------------"

""  # Recomenda-se que o nome do modelo teste tenha o nome do modelo no arquivo [ models.py ] + TestCase
""  # O modelo a ser testado não é importado, pois quem fará o trabalho de modelo é o [ model Mommy ]


def test_models():
    """
    ------------------------------------------------------- OBS -------------------------------------------------------
    -> self.var = mommy.make('Modelo') = simulação da criação de um objeto de um modelo específico
    -> self.var.texto                  = único campo do modelo criado acima em: CONFIGURAÇÕES INICIAIS

    from django.test import TestCase
    from model_mommy import mommy

    class ModeloTestCase(TestCase):
        def setUp(self):
            self.var = mommy.make('Modelo')

        def test_str(self):
            self.assertEquals(str(self.var), self.var.texto)
    """


"----------------------------------------------- EXEMPLO DE TESTE COMUM -----------------------------------------------"


def exemplo_teste_comum():
    """
    from django.test import TestCase

    def remover_vogais(string):
        container = []

        vowels = ['a', 'e', 'i', 'o', 'u',
                  'à', 'á', 'â', 'ã',
                  'é',
                  'í',
                  'ó', 'ô', 'õ', 'ò'
                  'ú',
                  ]

        for lt in string:
            container.append(lt)
        for lt in vowels:
            while lt in container:
                container.pop(container.index(lt))
        container = ''.join(container)
        return container

    class FirstTestCase(TestCase):
        def setUp(self):
            self.texto = 'Lucas Farias Santos de Sousa'

        def test_remover_vogais(self):
            frase = remover_vogais(self.texto)
            self.assertTrue(frase == 'Lcs Frs Snts d Ss')
    """


"-------------------------------------------------- MAIS INFORMAÇÕES --------------------------------------------------"
""  # Meu curso Django na Udemy [ 61. Testando formulários ]
""  # Meu curso Django na Udemy [ 62. Testando views ]
