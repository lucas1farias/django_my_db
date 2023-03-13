

"""
Curso    || Programação Web com Python e Django Framework: Essencial
Seção    || 9. Relacionamentos entre modelos
Aula     || 82. Relacionamento Muitos para Muitos
Objetivo ||
"""


def models():
    """
    from django.contrib.auth import get_user_model

    # ________________________________________________ MODELO QUE PASSA ________________________________________________
    # Não foi preciso criar, é passado apenas o novo campo ao modelo que herda, junta com a importação de usuário

    # ________________________________________________ MODELO QUE HERDA ________________________________________________
    class Vehicle:
        ...
        driver = models.ManyToManyField(get_user_model())
    """


# ----------------------------------------------------- IMPORTANTE -----------------------------------------------------
def admin():
    """
    * (ERRO) The value of 'list_display[i]' must not be a ManyToManyField
    * (SIGNIFICADO) Campos do tipo "ManyToManyField" criados em "models.py", não são permitidos em "admin.py"

    * ========== SOLUÇÃO ==========
    * SUPOSIÇÕES:
    * Vamos supor que este seja o campo dentro de uma classe:    driver = models.ManyToManyField(get_user_model())
    * Quando ele for passado em "admin.py" com seu nome (driver), o erro em [1] será lançado
    * Para corrigir essa restrição, cria-se uma função no escopo da classe (supondo que seja "VehicleAdmin")

    * ========== FUNÇÃO ==========
    * O nome da função pode ser qualquer coisa, contanto que faça sentido
    def show_drivers(self, obj):
        return ', '.join([driver.username for driver in obj.driver.all()])

    show_drivers.short_description = 'Motoristas'

    * ========== COMPLEMENTAÇÃO ==========
    * O próprio campo é usado na função, e cada um dos objetos ao qual "driver" pertence, são convertidos
    * É preciso passar a função como campo em "list_display"
    * É preciso dar um nome legível à função, via: (nome_da_função.short_description = 'nome')
    """


def terminal():
    """
    * Os usuários também podem ser criados pelo template admin

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser (x2) (criar 2 users que fazem uso do campo "ManyToManyField")
    """


def template_admin():
    """
    * Supondo que tenhamos 2 objetos de carro
    * O campo (driver) foi add como (ManyToManyField) em (Vehicle), mas não foi registrado em (admin.py)
    * Por conta disso, ele não é visto no template admin
    * Ao entramos nos objetos de carro, podemos ver o campo (drivers) que têm um formato de seleção via (ctrl)
    * Segurando o (ctrl) e clicando com o (botão ->), os objetos podem ser selecionados e salvos
    * Nos objetos abaixo, tivemos motoristas distintos escolhidos

    9BG116GW04C400001	Hyundai	Logan	43277.00 (lucasf, mario)
    9BG116GW04C400002	Ford	Hb20	37627.00 (luigi, mario)
    """


def terminal_shell():
    """
    * Como o tipo de relacionamento é (muitos p/ muitos) é esperado que ao usar o atributo, ele acesse mais de 1 dado
    * Sendo assim, quando se usa, por exemplo (car_1st.drive), se obtêm os dados em forma de objeto criptografado
    * Sabendo que é esperado mais de um dado, então se usa (car_1st.drive.all())
    * Ou seja: (nome do atrib. + all())
    * Com (ManyToManyField), é possível criar critérios de filtragem (ver: # FILTRAGEM)
    * Os critérios envolvem o próprio objeto do motorista / objeto do motorista + __in (p/ filtragem de + de 1 objeto)
    * A sintaxe (distinct()) impede repetições possíveis, pois não são necessárias

    from app.models import *
    vehicles = Vehicle.objects.all()
    vehicles                -----> <QuerySet [<Vehicle: Logan>, <Vehicle: Hb20>]>
    car_1st = vehicles.first()
    car_2nd = vehicles.last()
    car_1st                 -----> <Vehicle: Logan>
    car_2nd                 -----> <Vehicle: Hb20>
    car_1st.driver.all()    -----> <QuerySet [<User: lucasf>, <User: mario>]>
    car_2nd.driver.all()    -----> <QuerySet [<User: mario>, <User: Luigi>]>

    car_1st_drivers = car_1st.driver.all()
    car_1st_drivers         -----> <QuerySet [<User: lucasf>, <User: mario>]>
    lucas = car_1st_drivers.first()
    mario = car_1st_drivers.last()
    lucas                   -----> <User: lucasf>
    mario                   -----> <User: mario>

    # --------------------------------------------------- FILTRAGEM ---------------------------------------------------
    cars_driven_by_lucas = Vehicle.objects.filter(driver=lucas)
    cars_driven_by_lucas    -----> <QuerySet [<Vehicle: Logan>]>
    cars_driven_by_mario = Vehicle.objects.filter(driver=mario)
    cars_driven_by_mario    -----> <QuerySet [<Vehicle: Hb20>, <Vehicle: Logan>]>

    cars_driven_by_lucas_and_mario = Vehicle.objects.filter(driver__in = car_1st_drivers)
    cars_driven_by_lucas_and_mario           -----> <QuerySet [<Vehicle: Logan>, <Vehicle: Hb20>, <Vehicle: Logan>]>
    cars_driven_by_lucas_and_mario_shaped = Vehicle.objects.filter(driver__in = car_1st_drivers).distinct()
    cars_driven_by_lucas_and_mario_shaped    -----> <QuerySet [<Vehicle: Logan>, <Vehicle: Hb20>]>
    """
