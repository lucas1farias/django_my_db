

"""
* É a "class based view" mais comum, juntamente com "View"
* Em "template_name" é passado o "nome do template" a ser criado que trabalhará em conjunto com a view
* View usada p/ exibir dados comuns, mais pode exibir dados de modelos

    from django.views.generic import TemplateView

    class IndexView(TemplateView):
        template_name = 'index.html'

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def get_context_data(self, **kwargs):
            context = super(IndexView, self).get_context_data(**kwargs)
            return context
"""
