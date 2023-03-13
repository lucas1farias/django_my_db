

"""
Curso    || Programação Web com Python e Django Framework: Essencial
Seção    || 9. Relacionamentos entre modelos
Aula     || 80. Relacionamento Um para Um
"""


def models():
    """
    * O modelo que passa herança, pela lógica, normalmente têm um campo (pode ter +)
    * Esse campo é passado como "OneToOneField" p/ outro modelo (neste contexto: Vehicle)
    * O nome do modelo que cria o campo passado, não precisa ser o mesmo nome usado no modelo que recebe
    * Por isso em (Chassi) o campo se chama (number) e em (Vehicle) se chama (chassi)

    # ________________________________________________ MODELO QUE PASSA ________________________________________________
    class Chassi(Base):
        number = models.CharField('Número', max_length=16, help_text='Código do carro')

        class Meta:
            verbose_name = 'Chassi'
            verbose_name_plural = 'Chassis'

        def __str__(self):
            return self.number

    # ________________________________________________ MODELO QUE HERDA ________________________________________________
    class Vehicle(Base):
        chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
        model = models.CharField('Modelo', max_length=30)
        price = models.DecimalField('Preço', max_digits=8, decimal_places=2)

        class Meta:
            verbose_name = 'Carro'
            verbose_name_plural = 'Carros'

        def __str__(self):
            return self.model
    """


def admin():
    """
    * O campo que será do tipo OneToOneField (chassi) é passado normalmente no modelo herdeiro (Vehicle)
    * No modelo fonte, o nome do campo é (number), no modelo receptor, o nome é (chassi)

    @admin.register(Chassi)
    class ChassiAdmin(admin.ModelAdmin):
        list_display = ('number',)


    @admin.register(Vehicle)
    class VehicleAdmin(admin.ModelAdmin):
        list_display = ('chassi', 'model', 'price')
    """


def template_admin():
    """
    * Temos 2 modelos: Chassi, Vehicle
    * PASSO 1 || Adicionar um número de chassi (criar um objeto) pelo link de "Chassi" (configurado em "admin.py")
    * PASSO 2 || Adicionar um veículo (criar um objeto) e atribuir a este objeto, um número de chassi (OneToOneField)
    * Por ter sido criada uma relação entre os 2 modelos, no passo 2, o atrib. (chassi) se torna um "dropdown"
    * A relação é do tipo "1 p/ 1", que em Django é representado por "OneToOneField"
    * Sendo assim, o modelo que cria o atrib. passado como herança, deve ser criado um objeto ANTES do objeto que recebe
    * Se (Chassi) possui atrib. (number), um objeto dele é criado ANTES de um objeto (Vehicle)
    * Caso contrário, quando for tentado criar um objeto (Vehicle), o atrib. (chassi) será um "dropdown" vazio
    * Qual o motivo do uso do uso do relacionamento "1 p/ 1"?
        -> Se levarmos em conta o significado literal de "relacionamento", ele significa monogâmia
        -> Se um objeto de (Chassi) for tentado ser atribuído a + de um objeto (Vehicle), ele não permitirá
        -> Portanto, temos um relacionamento onde 1 está p/ outro um, e nenhum outro alem destes 2
        -> Um veículo só pode ter um único núm. de chassi, ou seja, o mesmo núm. de chassi não pode possuir a 2 veículos
    """


def relacionamento():
    """
    * Em nenhum momento o modelo (Vehicle) é chamado, mas ele pode ser acessado
    * O acesso é possível justamente pelo relacionamento criado entre (Chassi) e (Vehicle)
    * Pelo objeto índice 0 de (Chassi), se consegue acessar o objeto (Vehicle) ao qual ele está relacionado
    * É criado um meio de acesso que não existe por padrão (aqui: .vehicle)

    python manage.py shell
    from app.models import *
    chassis = Chassi.objects.all()
    chassis = <QuerySet [
        <Chassi: 9BG116GW04C400001>, <Chassi: 9BG116GW04C400002>,
        <Chassi: 9BG116GW04C400003>, <Chassi: 9BG116GW04C400004>
    ]>

    chassis[0].number     ->    '9BG116GW04C400001'
    chassis[0].vehicle    ->    <Vehicle: Hb20>
    """
