

"""
* model           = qual o modelo que a view vai exercer influência
* success_message = não funciona de forma direta, sendo preciso um método "delete" p/ lançar a mensagem

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView

class EraseTask(SuccessMessageMixin, DeleteView):
    model = Tasks
    success_message = 'A tarefa foi removida!'
    success_url = reverse_lazy('user-tasks')
    template_name = 'erase_task.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EraseTask, self).delete(request, *args, **kwargs)
"""
