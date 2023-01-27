

"""
* model  = qual o modelo que a view vai exercer influência
* fields = qual os atributos do modelo que servirão de input a serem editados
* fields = basicamente deve receber todos os atribs mandatórios p/ editar um objeto do modelo alvo

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView

class AlterTask(SuccessMessageMixin, UpdateView):
    fields = ('task',)
    model = Tasks
    success_message = 'Sua tarefa foi editada!'
    success_url = reverse_lazy('user-tasks')
    template_name = 'alter_task.html'
"""
