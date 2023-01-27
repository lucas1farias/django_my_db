

"""
* Essa ação modifica a configuração padrão Django, mudando as rotas das views p/ suas respectivas aplicações
* Pelo método "path", é feita a migração, passando o nome do módulo "urls.py" que será criado no pacote app
* Criar o módulo "urls.py" no pacote app

    from django.urls import include

    urlpatterns = [
        path('', include('nome_do_pa.urls'))
    ]
"""
