

"""
* STATIC_URL       = url de onde os arquivos estáticos podem estar (nome é opcional, criar pasta na raiz com nome ==)
* STATIC_ROOT      = local de armazenamento dos arquivos estáticos p/ o modo de produção
* STATICFILES_DIRS = local de armazenamento dos arquivos estáticos p/ o modo de desenvolvimento

* Deste modo, arquivos de imagens, css, js, passam a ser reconhecidos pelo Django
* Ou seja, agora é possível chamar esses arquivos, os referenciando de forma externa ao template, via "path"
* Imagens      || <img src="path/nome_imagem.formato">
* Arquivos css || <link rel="stylesheet", type="text/css" href="path/nome_arquivo.css">
* Arquivos js  || <script type="text/javascript" src="path/nome_arquivo.js" ></script>

    from os import path

    STATIC_URL = '/static/'

    # Configurado manualmente e criado automaticamente após "python manage.py collectstatic"
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')

    STATICFILES_DIRS = [
        # Criada manualmente
        path.join(BASE_DIR, 'static')
    ]

# ___________________________________________________ MODO PRODUÇÃO ___________________________________________________
* Comando 1: Cria o diretório configurado em "pp/settings.py" em STATIC_ROOT, que cria uma cópia de STATICFILES_DIRS

    python manage.py collectstatic
    python manage.py collectstatic --clear
"""
