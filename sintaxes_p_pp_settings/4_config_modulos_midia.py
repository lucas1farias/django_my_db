

def importante():
    """
    * Em Django, há dois tipos de módulos: estáticos e mídia
    * Ambas são a mesma coisa, mas há uma diferença
    * Os módulos estáticos, são: conteúdos criados/configurados pelo desenvolvedor p/ uso no projeto
    * Os módulos de mídia, são: conteúdos que o usuário manda para o projeto, por intermédio do desenvolvedor
    * Módulo estático: arquivo css (feito pelo desenvolvedor)
    * Módulo de mídia: upload de uma imagem (enviado pelo usuário, configurado pelo desenvolvedor)
    """


def settings():
    """
    * MEDIA_URL  = Nome da pasta a ser configurada e buscada pelo Django para receber arquivos de mídia
    * MEDIA_ROOT = Onde o Django deve buscar para receber arquivos de mídia vindos do usuário

    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'media')
    """


def urls():
    """
    * A concatenação acontece junto à lista "urlpatterns"

    from django.conf.urls.static import static
    from django.conf import settings
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """
