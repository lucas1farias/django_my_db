

"""
Curso    || Programação Web com Python e Django Framework: Essencial
Seção    || 9. Relacionamentos entre modelos
Aula     || 81. Relacionamento Um para Muitos
Objetivo || Realizar uma filtragem mais dinâmica (com menor sobrecarga)
            Contexto: Uma montadora pode ser definida p/ vários carros (relacionamento 1 p/ muitos)
            Se eu quiser saber quais objetos de carro pertencem a uma montadora, isso pode ser feito de forma dinâmica
            Ao invés de fazer a filtragem pelo modelo (Vehicle), isso é feito pelo modelo (Assembler)
            Isso gera menos sobrecarga, pois (Assembler) possui muito menos objetos a serem percorridos
            Motivo? Por conta do relacionamento entre (Vehicle=quem recebe herança) e (Assembler=quem passa herança)
            Por meio desse relacionamento, é criada uma sintaxe exclusiva: (nome_modelo_minusculo + _set)
            Por essa sintaxe, todos os objetos de carro que tiverem um objeto montadora específico, são capturados
            Para entender melhor, ver o decorrer deste documento
"""


def models():
    """
    # ________________________________________________ MODELO QUE PASSA ________________________________________________
    # O campo "name" é passado à classe "Vehicle" como "assembler"
    # O campo "name" é uma representação do que seria "OneToManyField", que não existe no Django
    # A sintaxe, ao invés de ser "OneToManyField", será "ForeignKey"
    # Como funciona o relacionamento "um p/ muitos"?
    # A idéia é que uma montadora pode fabricar muitos tipos de veículos, e muitos veículos estão p/ uma montadora

    class Assembler(Base):
        name = models.CharField('Nome da distribuidora', max_length=50)

        class Meta:
            verbose_name = 'Montadora'
            verbose_name_plural = 'Montadoras'

        def __str__(self):
            return self.name

    # ________________________________________________ MODELO QUE HERDA ________________________________________________
    class Vehicle:
        ...
        assembler = models.ForeignKey(Assembler, on_delete=models.CASCADE)
    """


def admin():
    """
    * O modelo criado (Assembler) é add ao template admin

    @admin.register(Assembler)
    class AssemblerAdmin(admin.ModelAdmin):
        list_display = ('name',)
    """


def terminal():
    """
    python manage.py makemigrations
    python manage.py migrate
    """


def template_admin():
    """
    * Criar uma distribuidora
    * Criar um chassi
    * Criar um veículo (dependente dos 2 campos acima)
    * Desconectar do servidor e entrar no Django Shell p/ testar a filtragem
    """


def relacionamento():
    """
    * Por causa do relacionamento (1 p/ muitos) criado em (Assembler) e passado p/ (Vehicle), é ganhado um acesso
    * Ao acessar um objeto de (Assembler), por ele, você pode acessar os objetos de veículos (Vehicle) que o usam
    * Primeiro, é preciso escolher o objeto (Assembler), que é feito na instanciação da var (assembler)
    * O acesso é feito como mostrado em (assembler_cars), onde (vehicle_set) não existiria sem o relacionamento
    * A configuração do acesso é pelo nome do modelo que recebe herança + _set: (vehicle_set)
    * Se, por exemplo, o modelo se chamasse (Mock), o acesso seria (mock_set), + por ser (Vehicle), então (vehicle_set)
    * Adicionalmente, é incluído um (.all()) p/ ter acesso a todos os objetos de veículos
    * Esse acesso cria um (queryset), que contêm todos os objetos de veículos que usam o objeto (assembler) como valor
    * Por um único objeto (var "assembler"), temos acesso a todos os objetos (var "assembler_cars")

    python manage.py shell
    from app.models import *
    assembler = Assembler.objects.get(pk=2)
    assembler                           -----> <Assembler: Hyundai>
    assembler_cars = assembler.vehicle_set.all()
    assembler_cars                      -----> <QuerySet [<Vehicle: Logan>]>
    assembler_cars.first()              -----> <Vehicle: Logan>
    assembler_cars.first().assembler    -----> <Assembler: Hyundai>
    assembler_cars.first().chassi       -----> <Chassi: 9BG116GW04C400001>
    """
