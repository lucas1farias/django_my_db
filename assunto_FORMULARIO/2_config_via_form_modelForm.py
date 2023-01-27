

def parte_1_config_modelo():
    """
    * A classe "Base" é criada somente p/ passar a classe "Meta" a outras classes herdeiras
    * O que é preciso saber?
    * O modelo alvo é "Language", ele conversará com um modelo de formulário em "pa/forms.py" (é criado e configurado)
    * A comunicação se dá pelos atributos criados em "Language" que são passados igualmente p/ o "ModelForm"
    * Mais infos: ver parte 4

    from django.db import models

    class Base:
        class Meta:
            abstract = True

    class Language(models.Model, Base):

        name = models.CharField('Nome', max_length=100)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Linguagem'
            verbose_name_plural = 'Linguagens'
    """


def parte_2_registro_modelo_template_admin():
    """
    * O modelo + os atributos desejados a serem exibidos, são passados

    from django.contrib import admin
    from .models import *


    @admin.register(Child)
    class ChildAdmin(admin.ModelAdmin):
        list_display = ('name',)
    """


def parte_3_criar_validar_modelo():
    """
    python manage.py makemigrations
    python manage.py migrate
    """


def parte_4_criar_configurar_modulo_forms():
    """
    * O modelo é importado p/ este módulo
    * Os atribs. do modelo são passado do modelo fórmulário "LanguageModelForm"
    * Neste exemplo, temos somente um atrib., mas poderiam ser vários (todos os usados devem ser instanciado aqui)
    * O(s) atrib(s). que for(em) se tornar input(s), são passados a tupla (fields)

    * IMPORTANTE
    * O atributo "name" deste exemplo, se torna um input no template com o atrib. (name="nome_do_atrib_na_classe")
    * Além do atrib. se tornar um atrib. no input do template, também é add um atrib. (id="id_nome_do_atrib_na_classe")

    from django import forms
    from .models import *

    class LanguageModelForm(forms.ModelForm):
        class Meta:
            model = Language
            fields = ('name',)
            name = forms.CharField(max_length=100)
    """


def parte_5_config_view():
    """
    * Onde a view é criada, o formulário é importado, e junto dele o modelo também é
    * Como a view é do tipo "FormView", as vars. "form_class" e "success_url" são necessárias, juntos suas bibliotecas
    * Como a view é do tipo "FormView", as funções "form_valid" e "form_invalid" se tornam acessíveis
    * As funções acima tratam cada input p/ impedir que fiquem faltando dados
    * O formulário modelo (aqui: LanguageModelForm) cria um formulário com base nas suas configurações
    * Exemplo: cada input recebe o atributo "required" e um "id=id_nome_atrib_na_classe_do_formulario_modelo"
    * A função "get_last_object_data" é opcional e serve aqui apenas p/ demonstrar que o formulário funciona
    * A função "get_last_object_data" trabalha em conjunto com: "__init__" e "get_context_data"

    from django.views.generic import FormView
    from .forms import *
    from django.urls import reverse_lazy
    from django.contrib import messages

    class LanguageFormView(FormView):
        template_name = 'model_form.html'
        form_class = LanguageModelForm
        success_url = reverse_lazy('model_form')  # nome do url desta view

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.db = Language.objects.all()
            self.last_object = ''

            if len(self.db) == 0:
                mock_obj = Language(name='Python')
                mock_obj.save()
            else:
                self.last_object = self.get_last_object_data()

        def get_last_object_data(self) -> str:
            db_size = len(self.db) - 1
            last_object_from_db = None

            for pos, index in enumerate(self.db):
                # Se chegar no último índice do banco, pegar o atributo deste objeto neste índice
                if pos == db_size:
                    last_object_from_db = self.db[pos].name

            # Porque usar 'filter'? por lidar com objetos repetidos, enquanto 'get' só lida com um objeto
            # Enquanto 'get' só achar uma ocorrência, seu uso é melhor, mas quando houver objetos repetidos, ele gera erro
            last_input = Language.objects.filter(name=last_object_from_db)
            return last_input[0].name

        def form_valid(self, form):
            print(dir(form))
            print('--->', form.cleaned_data.get('name'))
            form.save()
            messages.success(self.request, 'Linguagem enviada')
            return super(LanguageFormView, self).form_valid(form)

        def form_invalid(self, form):
            messages.error(self.request, 'Erros nos campos')
            return super(LanguageFormView, self).form_invalid(form)

        def get_context_data(self, **kwargs):
            context = super(LanguageFormView, self).get_context_data(**kwargs)
            context['db'] = self.db
            context['input_value'] = self.last_object
            return context
    """


def parte_6_config_url():
    """
    path('model_form', LanguageFormView.as_view(), name='model_form')
    """


def parte_7_config_template():
    """
    * A view configurada como "FormView" permite que o formulário seja chamado no template como {{ form }}
    * O atributo "action" remete a própria página. Se fosse p/ ir a outra lugar, se passa o url de outro template
    * O atributo "method" sempre é "post", o que indica que o formulário está a receber dados
    * O envio se dá por botão ou input, ambas formas funcionam

    <section>
        <div>
            <h2>Teste de formulário com model form Django</h2>
            <h5>Ordem: models.py, admin.py, forms.py, views.py, urls.py, template</h5>

            <form action="{% url 'model_form' %}" method="post">
                {% csrf_token %}
                {{ form }}

                <button type="submit">Enviar (via button)</button>
                <input type="submit" value="Enviar (via input)">
            </form>

            <div>Último dado enviado:<span class="btn btn-success">{{ input_value }}</span></div>
        </div>
    </section>
    """
