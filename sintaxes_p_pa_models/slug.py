

def objetivo():
    """
    * Criar uma url dinâmica com base em algum campo de "nome-composto" dentro de alguma classe
    * Isso pode servir para acessar vários objetos de um modelo, tendo cada um sua url dinâmica
    * "Slugify" significa converter espaços em branco em traços
    * MOTIVO? urls não possuem espaço, e slugs são majoritariamente usadas para serem urls
    * Ex: campo = 'Ana é pequena' se torna slug = 'ana-e-pequena'
    """


def models():
    """
    from django.db import models
    from django.utils.text import slugify

    class Person(admin.ModelAdmin):
        name = models.CharField('Nome', help_text='Limite: 50 caracteres', max_length=50)
        slug = models.SlugField('Complemento', blank=True, null=True)

        class Meta:
            verbose_name = 'Pessoa'
            verbose_name_plural = 'Pessoas'

        def __str__(self):
            return self.name

        def save(self, *args, **kwargs):
            if self.slug is None:
                self.slug = slugify(self.name)
            super().save(*args, **kwargs)
    """


def template_admin():
    """
    * Entrar no modelo e adicionar um novo objeto. Ao redirecionar, o campo "slug" terá sido preenchido
    * Isso se dá pela função "save" criada no escopo de "Person"
    * A função só funciona pela importação do "slugify"
    * Na função, o campo "slug" é verificado, e estando vazio, seu valor se torna a "slugificação" do campo "name"
    """
