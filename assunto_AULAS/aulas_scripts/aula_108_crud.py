

"""
Módulo: aula_108_crud.py
"""

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 12:Adicionando outras funcionalidades
    Aula:   # 108. Criando um CRUD com Class Based View
    """

def terminal():
    """
    pip install django==2.2.8  # na época da aula, essa era a versão do django lts mais atual
    pip install django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

# No template, 'django.contrib.humanize' é passado como: {% load humanize %}
def settings():
    """
    INSTALLED_APPS = ['bootstrap4', 'pa', 'django.contrib.humanize']
    TEMPLATES = [{'DIRS': ['templates']}]
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('', IndexListView.as_view(), name='index'),
        path('criar/', ProductCreateView.as_view(), name='criar/'),
    ]
    """

def models():
    """
    from django.db import models

    class Product(models.Model):
        name = models.CharField('Nome', max_length=150)
        price = models.DecimalField('Preço', decimal_places=2, max_digits=9)

        class Meta:
            verbose_name = 'Produto'
            verbose_name_plural = 'Produtos'

        def __str__(self):
            return self.name
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ('name', 'price')
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """

# Não existe, cria-se em pa
"É preciso ter muito cuidado ao criar formulário modelo, pois ele pode ser confundido com formulário"
def forms():
    """
    from django import forms
    from .models import *

    class ProductModelForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = ('name', 'price')
    """

# A variável [ context_object_name ] == [ context = {} ], e o valor da variável é usado no template
"Ex: {% for each_data in produtos %}{% endfor %}"
def views():
    """
    from django.views.generic import ListView
    from .models import *

    class IndexListView(ListView):
        context_object_name = 'produtos'
        models = Product
        queryset = Product.objects.all()
        template_name = 'index.html'
    """

# index.html (onde estão as tabelas e seus campos)
"{{ each_data.price|intcomma }} = método do {% load humanize %} para corrigir classificações numéricas de cada língua"
def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
        <style>body {background-color: #222; color: white;}</style>
    </head>
    <body>
    {% load humanize %}
    {% bootstrap_messages %}
        <div class="container text-center">
            <div class="mt-2"><i class="border border-danger px-2 py-2">{{ current_date }}</i></div>
            <h2 class="mt-5">Produtos</h2>
            <div>adicionados: <i>{{ countage }}</i></div>
            <div class="container-fluid text-right">
                <p><a class="btn btn-primary text-white" href="{% url 'criar/' %}" style="border-radius: 50%;">+</a> via input normal</p>
                <p><a class="btn btn-primary text-white" href="{% url 'criar2/' %}" style="border-radius: 50%;">+</a> via bootstrap_form</p>
            </div>
            <table class="table table-dark table-bordered">
                <thead class="text-center">
                    <tr>
                        <th>#</th>
                        <th>Nome</th>
                        <th>Preço</th>
                        <th>Ação</th>
                    </tr>
                </thead>
                <tbody>
                    {% for each_data in produtos %}
                    <tr>
                        <td>{{ each_data.id }}</td>
                        <td>{{ each_data.name }}</td>
                        <td>{{ each_data.price|intcomma }}</td>
                        <td class="text-center">
                            <a class="btn btn-primary text-white" href="#">editar</a>
                            <a class="btn btn-danger text-warning" href="#">deletar</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
                <tfoot></tfoot>
            </table>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# success_url = reverse_lazy('rota')
"se o formulário for preenchido com sucesso, redirecionar (mandatório nesse tipo de view)"
def views2():
    """
    from django.urls import reverse_lazy
    from django.views.generic import CreateView

    class ProductCreateView(CreateView):
        fields = ('name', 'price')
        model = Product
        success_url = reverse_lazy('index')
        template_name = 'modelform-product'
    """

# criar.html (onde cria-se um objeto novo de um bdd, via input normal)
def templates2():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
        <style>.ma {margin: auto;} .btn-dark:hover a{text-decoration: none;}</style>
    </head>
    <body>
        <div class="container">
            <h2 class="mb-5 mt-5 text-center text-primary">Novo produto</h2>
            <form action="{% url 'criar/' %}" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <div class="form-group">
                    <div class="col-6 col-sm-6 col-md-6 col-lg-6 col-xl-6 ma">
                        <input class="form-control mb-2" name="name" placeholder="nome do produto" type="text">
                        <input class="form-control mb-2" name="price" placeholder="preço do produto" step="0.01" type="number">
                        <button class="btn btn-dark mt-3" form="this-form" type="submit">
                            <a class="text-white">Salvar</a>
                        </button>
                        <a class="btn btn-danger mt-3 text-white" href="{% url 'index' %}">Voltar</a>
                    </div>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# Já há uma view class based view para criar um objeto, mas vamos criar um objeto via function based view também
def pa_urls2():
    """ urlpatterns = [path('criar2/', product_create_view, name='criar2/')] """

# product_create_view
def views3():
    """
    from django.shortcuts import redirect
    from .forms import *

    def product_create_view(request):
        create_object = ProductModelForm(request.POST or None)
        if str(request.method) == 'POST':
            if create_object.is_valid():
                create_object.save()
                create_object = ProductModelForm()
                messages.success(request, 'Novo produto adicionado')
                return redirect('index')
            else:
                messages.error(request, 'Produto não adicionado')
        else:
            create_object = ProductModelForm()

        context = {'create_object': create_object}
        return render(request, 'criar2.html', context)
    """

# index.html (o template já existe, mas vamos adicionar a rota da nova view, na view matriz)
def templates3():
    """
    <p><a class="btn btn-primary text-white" href="{% url 'criar2/' %}" style="border-radius: 50%;">+</a> via bootstrap_form</p>
    """

# criar2.html (onde cria-se um objeto novo de um bdd, via bootstrap_form)
def templates4():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
        <style>.ma {margin: auto;} .btn-primary:hover a{text-decoration: none;}</style>
    </head>
    <body>
        <div class="container">
            <h2 class="mb-5 mt-5 text-center text-primary">Novo produto - método 2</h2>
            <form action="{% url 'criar2/' %}" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <div class="row">
                    <div class="col-6 col-sm-6 col-md-6 col-lg-6 col-xl-6 ma">
                        {% bootstrap_form create_object %}
                        <button class="btn btn-primary mt-3" form="this-form" type="submit">
                            <a class="text-white">Salvar</a>
                        </button>
                        <a class="btn btn-danger mt-3 text-white" href="{% url 'index' %}">voltar</a>
                    </div>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# 1. O template criado para criar um objeto novo, pode ser o mesmo que o atualiza
" 2. Apesar das views cbv terem as mesmas variáveis e serem idênticas, suas funções são diferentes"
# 3. Uma cbv CreateView gera um objeto e seu id, enquanto uma cbv UpdateView edita um objeto baseado no seu id
def views4():
    """
    from django.views.generic import UpdateView

    class ProductUpdateView(UpdateView):
        fields = ('name', 'price')
        model = Product
        success_url = reverse_lazy('index')
        template_name = 'criar.html'
    """

# Apesar de receber um template que já existe, a view precisa de uma rota única para si
def pa_urls3():
    """ urlpatterns = [path('<int:pk>/alterar/', ProductUpdateView.as_view(), name='alterar/')] """

# index.html
" 1. Anteriomente um botão de editar foi criado no template, mas estava sem uma rota, agora vamos adicionar"
# 2. Lógica: href="{% url 'name=' 'var1_loop_for.método' %}"
" 3. Ou seja, esse tipo de contexto só acontece quando ha um loop for presente no template"
def templates5():
    """ <a class="btn btn-primary text-white" href="{% url 'alterar/' each_data.pk %}">editar</a> """

def fora_contexto():
    """"""
    # views.py
    "from datetime import datetime"

    # views.py -> IndexListView
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = datetime.now()
        context['countage'] = Product.objects.all().count()
        return context
    """

    # index.html
    """
    <div class="mb-2"><i class="border border-danger px-2 py-2">{{ current_date }}</i></div>
    <div>Produtos adicionados: <i>{{ countage }}</i></div> 
    """
