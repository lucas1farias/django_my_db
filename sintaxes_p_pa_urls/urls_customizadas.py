

"""
* São urls que recebem sintaxes de tipagem e o nome do atributo que serão mesclados nessa url
* QUANDO USAR? Quando objetos de um modelo forem exibidos e precisam ser acessados p/ algum CRUD
* EX:
    -> path('alter-task/<int:pk>', AlterTask.as_view(), name='alter-task')

    -> Tudo começa com a view (aqui: AlterTask) que faz as configurações p/ manipular os objetos do modelo
    -> Primeiro, é preciso informar a view qual o modelo que ela irá exercer influência
    -> Tudo aquilo que for desejado alterar num objeto, deve ser passado à var "fields"
    -> Como nesse contexto, o modelo só possui o atrib "task", então só ele é passado
    -> Para CADA ATRIB em "fields" deve ter um input correspondente no template responsável por editar este objeto
    -> Se neste exemplo, o atrib é "task", então no template deve ter um <input name="task">
    -> O template é == p/ todos os objetos, mas cada um obtêm o seu separado por 2 motivos
    -> MOTIVO 1: A sintaxe "path" na seta do topo (pa/urls.py) que passa um atrib "pk" que é != p/ cada objeto
    -> MOTIVO 2: Sua chamada na tag <a href="{% url 'alter-task' task.pk %}">editar</a> que finaliza a configuração
    -> Se a escolha for um atrib !=, na sintaxe da seta do topo, se deve mudar o tipo e o nome (ex: /<str:task>)

class AlterTask(SuccessMessageMixin, UpdateView):
    model = Tasks
    fields = ('task',)
    template_name = 'alter_task.html'
    success_message = 'Sua tarefa foi editada!'
    success_url = reverse_lazy('user-tasks')
"""
