

"""
* Modelos Django não criam atributos de classe, mas variáveis de classe

    class Sign(Base):
        # Atributo(s)
        birthday = models.CharField('Aniversário', max_length=100)

        # Representação do objeto
        def __str__(self):
            return self.birthday

        # Rótulos p/ o Django template admin (p/ explicar sobre o que o modelo representa)
        class Meta:
            verbose_name = 'Aniversário'
            verbose_name_plural = verbose_name + 's'
"""
