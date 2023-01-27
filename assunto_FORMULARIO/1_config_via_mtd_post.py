

"""
* O método "post" Django é um método que consegue resgatar dados de inputs via seu parâmetro: "request"
* Isso só é possível se uma view Django com um método "post" e que aponte p/ um template que tenha um formulário (input)
* RESGATE: "request.POST['valor_do_atrib_name_no_input_do_template']"
* VALIDAÇÃO: atributo "required" inserido nos inputs desejados
* self.name = valor que receberá o valor submetido pelo botão que envia o formulário (dados passados nos inputs)
* Quando o usuário clica no botão de envio do formulário, o método "post" é requisitado na view
* O valor passado no input é resgatado via "request", atribuido a "self.name", cria o obj e o envia ao bdd
* O valor pode ser apresentado via "get_context_data" (opcional), atribuindo uma chave a "self.name"

from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import *

# ________________________________________________________ VIEW ________________________________________________________
    class IndexView(TemplateView):
        template_name = 'index.html'

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.name = ''

        def post(self, request):
            if str(request.method) == 'POST':
                self.name = request.POST['tag_input_atrib_name_value']
                obj = Model(name=self.name)
                obj.save()
                return redirect('index')

        def get_context_data(self, **kwargs):
            context = super(IndexView, self).get_context_data(**kwargs)
            context['name_self'] = f'Var. self: {self.name}'
            return context

# _______________________________________________ FORMULÁRIO NO TEMPLATE _______________________________________________
* Os botões não precisam estar dentro do formulário
* O input que terá valor transformado em objeto é repr. pelo valor do atrib. "name", e por ele, o back-end é feito
* A sintaxe {%%} é mandatória, caso contrário, Django gera erro "Forbidden"

    <section>
        <div class="inputs-set">
            <form action="{% url 'index' %}" autocomplete="off" method="post">
            {% csrf_token %}
                <div><input type="text" max="100" min="2" name="first_name" placeholder="Seu nome" required></div>
                <button type="submit">Enviar dados ao back-end (botão)</button>
                <input type="submit" value="Enviar dados ao back-end (botão input)">
            </form>
        </div>
    </section>
"""
