

"""
* No "pacote app", criar um módulo "urls.py"
* Todas as views criadas que forem usadas, são importadas a este módulo
* (par 1) vazio por ser a página inicial, mas normalmente recebe o mesmo nome que "par 3"
* (par 3) name = parâmetro que diz ao Django qual o sufixo/slug/url de acesso a view que o acompanha

    from django.urls import path
    from .views import IndexView

    urlpatterns = [
        path('', IndexView.as_view(), name='index')
    ]
"""
