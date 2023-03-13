

def parametros_padrao():
    """
    OBS       || Todos os campos de modelo Django possuem 2 parâmetros padrão
    par_1     || String p/ explicar a descrição do campo no template admin (rótulo do input)
    help_text || String p/ instrução (exemplo, detalha extra sobre o campo)
    """


class BooleanField:
    """
    default || Configura um checkbox p/ informar a disponibilidade de um objeto no template admin
    sintaxe || models.BooleanField('Disponibilidade', help_text='', default=True)

    * ===== AUTOMATIZAR CONTROLE DE QUANTIDADE =====
    * Supondo que o objeto seja um produto e ele possui um estoque
    * Uma função que poderia controlar/monitorar isso

    def save(self, *args, **kwargs):
        if self.storage > 0:
            self.availability = True
        if self._integer <= 0:
            self.availability = False
        super().save(*args, **kwargs)
    """


class CharField:
    """
    max_length || Qtd. máxima de caracteres que o campo (caso seja texto) deve ter
    sintaxe    || models.CharField('Descrição', help_text='', max_length=100)
    """


class DateTimeField:
    """
    auto_now_add || Configura p/ que seja exibida os dados da criação do objeto ao modelo
    auto_now     || Configura p/ que seja exibida os dados da última vez que o objeto sofreu alguma alteração
    sintaxe      || models.DateTimeField('Data de criação', auto_now_add=True)
    sintaxe      || models.DateTimeField('Última atualização', auto_now=True)
    """


class DecimalField:
    """
    par_1          || Descrição apresentada no template admin (rótulo do input)
    decimal_places || Qtd. de casa decimais após a vírgula
    max_digits     || Qtd. máxima de dígitos permitidos antes das casa decimais
    sintaxe        || models.DecimalField('Descrição', decimal_places=2, max_digits=8)
    """


class FloatField:
    """
    par_1   || Descrição apresentada no template admin (rótulo do input)
    sintaxe || models.FloatField('Descrição')
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


class IntegerField:
    """
    par_1   || Descrição apresentada no template admin (rótulo do input)
    sintaxe || models.IntegerField('Descrição')
    """


# MAIS INFOS: sintaxes_p_pa_models/relacionamentos/OneToOneField.py
class OneToOneField:
    """
    OBS     || Nessa contexto, temos 2 modelos envolvidos (relacionamento)
    OBS     || O modelo servidor, apenas cria o campo que servirá o modelo receptor
    OBS     || O modelo servidor cria o campo normalmente, enquanto o receptor recebe "models.OneToOneField"
    par 1   || Especificar qual o modelo servidor (aquele que oferta o campo p/ o relacionamento)
    sintaxe || models.OneToOneField(Modelo, on_delete=models.CASCADE)

    class Chassi(Base):
        number = models.CharField('Número de série do veículo', help_text='17 caracteres' max_length=20)

    class Vehicle(Base):
        chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    """


class SlugField:
    """
    * Esse campo costuma ser configurado com os parâmetros "blank" e "null"
    * Isso acontece, pois o campo de "slug" é uma forma interessante de obter um "url dinâmico"
    * Supondo que um objeto seja um produto, ele possui os campos: name, slug
    * name = "copo de plástico" ... slug = ''
    * Uma função dentro do modelo que cria o objeto, pode ser configurada p/ passar o campo "name" p/ o campo "slug"
    * RESULTADO: name = "copo de plástico" ... slug = "copo-de-plastico"
    * ===== FUNÇÃO =====
    * A biblioteca Python "uuid4" pode ajudar na complementação do slug

    from django.utils.text import slugify
    from uuid import uuid4

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name) + f'-{uuid4()}'
        super().save(*args, **kwargs)

    blank   || Determina que o campo não possui nenhum valor (python o considera como "None")
    null    || Determina que o campo não é acessível no template admin do Django
    sintaxe || models.SlugField('Complemento', blank=True, null=True)
    """


class TextField:
    """
    OBS        || Idêntico ao "CharField", com exceção do tamanho do input (que é grande)
    max_length || Qtd. máxima de caracteres que o campo (caso seja texto) deve ter
    sintaxe    || models.CharField('Descrição', help_text='', max_length=100)
    """
