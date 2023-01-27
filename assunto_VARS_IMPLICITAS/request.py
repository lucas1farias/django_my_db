

"""
* Var que serve de parâmetro tanto em "function based view" quanto em "class based view"
* Em "function based view" é passado como "request", já em "class based view", é passada como "self.request"

# __________________________________________________ Class based view __________________________________________________
class RequestView(TemplateView):
    template_name = 'request_cbv.html'

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        context['request_cbv'] = dir(self.request)
        context['request_user'] = dir(self.request.user)
        return context

# ________________________________________________ Function based view ________________________________________________
def request_view(request):
    context = {
        'request': dir(request),
        'request_user': dir(request.user)
    }
    return render(request, 'request.html', context)

# _______________________________________________________ Rotas _______________________________________________________
path('request', request_view, name='request'),
path('request_cbv', RequestView.as_view(), name='request_cbv')

# _________________________________________________ Templates (ambos) _________________________________________________
<div>{{ request_cbv }}</div>
<div>{{ request }}</div>
<div>{{ request_user }}</div>
"""
