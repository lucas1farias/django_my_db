

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
    * Por padrão, todo projeto Django já possui a constante "STATIC_URL"
    * STATIC_URL       = dir. onde os arquivos estáticos estarão (o nome é opcional)
    * STATIC_URL       = o valor que for passado a essa constante, deve ser o nome exato do dir. criado na raiz
    * STATIC_ROOT      = local de armazenamento dos arquivos estáticos p/ o modo de produção
    * STATIC_ROOT      = esta constante é configurada manualmente (criação da constante)
    * STATIC_ROOT      = a pasta configurada é criada após DEBUG = False + python manage.py collectstatic
    * STATICFILES_DIRS = local de armazenamento dos arquivos estáticos p/ o modo de desenvolvimento
    * STATICFILES_DIRS = esta constante é configurada manualmente (criação da constante e da pasta)

    from os import path
    STATIC_URL = '/static/'
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
        path.join(BASE_DIR, 'static')
    ]
    """


def objetivos():
    """
    * Permitir que arquivos de imagens, css, js, passam a ser reconhecidos pelo Django
    * Referenciar arquivos estáticos dentro de templates sem estarem neles
    * Imagens      || <img src="path/nome_imagem.formato">
    * Arquivos css || <link rel="stylesheet", type="text/css" href="path/nome_arquivo.css">
    * Arquivos js  || <script type="text/javascript" src="path/nome_arquivo.js" ></script>
    """


def terminal_modo_producao():
    """
    * Comando 1: Cria a pasta configurada na constante "STATIC_ROOT"
    * Comando 1: Todos os arquivos estáticos configurados na pasta definida na constante STATIC_URL são copiados
    * Comando 1: Os arquivos copiados, são enviados à pasta definida na constante "STATIC_ROOT"
    * Comando 2: Limpa a pasta configurada na constante "STATIC_ROOT"

    . python manage.py collectstatic
    . python manage.py collectstatic --clear
    """
