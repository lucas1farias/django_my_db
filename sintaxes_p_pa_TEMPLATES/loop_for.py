

"""
Uso mais comum: Exibir objetos de um modelo
Uso menos comum: Exibir iteráveis de algoritmos passados pelas vars. de contexto
[1] Exemplo com modelo e seus objetos (não necessariamente precisa estar numa função __init__)
[2] Exemplo com iterável

    # ______________________________________________________ VIEW ______________________________________________________
    from .models import Nouns

    class IndexView(TemplateView):
        template_name = 'index.html'

        def __init__(self, **kwargs):
            # [1]
            self.db = Nouns.objects.all()

            # [2]
            self.options = {
                '1': f'1 - {str(self.nouns_array[0].translation)}',
                '2': f'2 - {str(self.nouns_array[1].translation)}',
                '3': f'3 - {str(self.nouns_array[2].translation)}',
                '4': f'4 - {str(self.nouns_array[3].translation)}',
                '5': f'5 - {str(self.nouns_array[4].translation)}',
            }


        def get_context_data(self, **kwargs):
            context = super(IndexView, self).get_context_data(**kwargs)
            # [1]
            context['db'] = self.db

            # [2]
            context['options'] = self.options
            return context

    # ____________________________________________________ TEMPLATE ____________________________________________________
    {% for option in options.values %}
        <div>{{ option }}</div>
    {% endfor %}

    {% for index in db %}
        <div>{{ index }}</div>
    {% endfor %}
"""
