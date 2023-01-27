

"""
* Modelo que trás informações que podem ser úteis sobre a criação do algum objeto
* Ele é passado por herança p/ outros modelos e não precisa ser registrado em "pa/admin.py"
* Além da herança, p/ ele ser visível em outro modelo, usar os seus atribs. em "pa/admin.py" (ex. abaixo)

    class Base(models.Model):
        created = models.DateTimeField('Data de criação', auto_now_add=True)
        updated = models.DateTimeField('Última atualização', auto_now=True)
        availability = models.BooleanField('Disponibilidade', default=True)

        class Meta:
            abstract = True

* pa/admin.py
* Para ver os campos desse modelo em outros, os campos abaixo são anexados na tupla de config. do outro modelo
    list_display = ('created', 'updated', 'availability')
"""
