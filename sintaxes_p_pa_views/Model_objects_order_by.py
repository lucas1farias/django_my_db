

"""
* Exibir objetos de um modelo numa view, de forma que eles se apresentem em critérios aleatórios
* Sintaxe normal   || Model.objects.all()
* Sintaxe alterada || Model.objects.order_by('?').all()
* Instanciação preferencialmente no método __init__ ou no método "get_context_data"

def get_context_data(self, **kwargs):
    context = super(View, self).get_context_data(**kwargs)
    context['modelo'] = Model.objects.order_by('?').all()
    return context
"""
