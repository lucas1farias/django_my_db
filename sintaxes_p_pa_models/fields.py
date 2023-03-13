

class CharField:
    """
    par_1      || Descrição apresentada no template admin (rótulo do input)
    help_text  || Texto de instrução p/ caso um campo não esteja claro o suficiente (pode descrever um exemplo)
    max_length || Qtd. máxima de caracteres de uma string
    sintaxe    || models.CharField('Descrição', help_text='', max_length=100)
    """


class DecimalField:
    """
    par_1          || Descrição apresentada no template admin (rótulo do input)
    decimal_places || Qtd. de casa decimais após a vírgula
    max_digits     || Qtd. máxima de dígitos permitidos antes de casa decimais
    sintaxe        || models.DecimalField('Descrição', decimal_places=2, max_digits=8)
    """


class ImageField:
    """
    * ===== Terminal =====
    * Biblioteca "pillow" (pip install pillow) + configuração de MEDIA_URL e MEDIA_ROOT em "settings.py" e "urls.py"

    * ===== settings.py =====
    * MEDIA_URL  = Nome da pasta a ser configurada e buscada pelo Django para receber arquivos de mídia
    * MEDIA_ROOT = Onde o Django deve buscar para receber arquivos de mídia vindos do usuário

    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'media')

    * ===== urls.py =====
    * A concantenação é junta à variável "urlpatterns"

    from django.conf.urls.static import static
    from django.conf import settings
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    * ===== Função =====
    * Criar nomes customizados para imagens de upload do usuário usando: datetime strftime + nome_arquivo + uuid4
    * Deve ser criada no mesmo nível das classes em "models.py"

    def mock_name(instance, filename):
        extension = [*str(filename).split('.')]
        #  print(extension)
        #  print(extension[0])
        return datetime.now().strftime('%Y-%m-%d-%H-%M-') + f'{extension[0]}-{uuid4()}.{extension[1]}'

    upload_to || As configurações no "terminal", "settings" e "urls", se dá pelo uso deste parâmetro
    upload_to || Normalmente o que é passado como valor neste parâmetro, é o mesmo nome dado à pasta MEDIA_URL
    upload_to || No entanto, há a possibilidade de objetos criados terem o mesmo nome (o que é algo ruim)
    upload_to || Além das configurações já descritas, é melhor ter uma função que cria nomes customizados p/ as imagens
    upload_to || Por causa das configurações acima, este parâmetro já irá enviar as imagens p/ MEDIA_URL
    upload_to || Então, ao invés de "upload_to" apontar para "MEDIA_URL", ele apontará para a função (mock_name)
    upload_to || Fazendo isso, o nome das imagens serão todas diferentes (quase impossível acontecer repetição)
    sintaxe   || (FORMA 1) models.ImageField('Descrição', upload_to='', blank=True, null=True)
    sintaxe   || (FORMA 2) models.ImageField('Descrição', upload_to=mock_name, blank=True, null=True)
    """


def integer_field():
    """
    par_1   || Descrição do que o número registrado será atrelado (ex: Número da casa)
    sintaxe || models.IntegerField('Descrição')
    """


# MAIS INFOS: sintaxes_p_pa_models/relacionamentos/OneToOneField.py
def one_to_one_field():
    """
    par 1   || Especificar qual o modelo ao qual este campo pertence (pela lógica, o modelo alvo só deve ter este campo)
    sintaxe || models.OneToOneField(Modelo, on_delete=models.CASCADE)
    """

