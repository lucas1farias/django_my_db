

"""
* Após criar o modelo, ele deve ser importado e registrado no módulo citado acima
* list_display = atribs. do modelo exibíveis no template admin
* Após registrar, é preciso os comandos p/ validar e criar o modelo (via terminal)

    from .models import *

    @admin.register(NomeModelo)
    class NomeModeloAdmin(admin.ModelAdmin):
        list_display = ('nome_atrib', 'nome_atrib', '...')
"""
