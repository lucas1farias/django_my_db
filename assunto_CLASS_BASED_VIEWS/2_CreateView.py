

"""
* model  = qual o modelo que a view vai exercer influência
* fields = qual os atributos do modelo que servirão de input
* fields = basicamente deve receber todos os atribs mandatórios p/ criar um objeto do modelo alvo

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

class NewTask(SuccessMessageMixin, CreateView):
    fields = ('task',)  # Campos do formulário a serem editados
    model = Tasks
    success_message = 'Uma nova tarefa foi adicionada!'
    success_url = reverse_lazy('user-tasks')
    template_name = 'create_task.html'
"""
