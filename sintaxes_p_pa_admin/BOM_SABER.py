

def admin_nao_precisa_validar():
    """
    Alterações no módulo "admin.py" não precisa dos comandos (python manage.py makemigrations & migrate)
    """


def exibir_campos_que_sao_iteraveis_nao_string():
    """
    * Observe a função estática (show_drivers)
    * Ela faz um tratamento de dados de um campo cujo relacionamento é (ManyToManyField)
    * Desse relacionamento, é costumeiro vir tuplas/listas e esses dados não são permitidos exibição no template admin
    * A função (show_drivers) trata essas tuplas/listas p/ que se tornem strings e que sejem exibidas no template admin
    * A função está acessando cada objeto (Vehicle) e acessando seu campo "ManyToManyField" (driver)
    * Ao ter todos os dados num iterável, eles são revertidos p/ string e assim podem ser exibidos no template admin
    * A função é passada como string em (list_display)
    * Ainda é possível dar um nome mais intuitivo a função, p/ evitar que ela apareça no template admin
    * Por isso, na última linha é trocado o nome da função por uma descrição, p/ melhor entendimento no template admin

    @admin.register(Vehicle)
    class VehicleAdmin(admin.ModelAdmin):
        list_display = (
            'chassi',     # vindo de (Chassi), mas em (Vehicle), se apresenta como (chassi)
            'assembler',  # vindo de (Assembler), mas em (Vehicle) se apresenta como (assembler)
            'model', 'price',
            'show_drivers'
        )

        def show_drivers(self, obj):
            return ', '.join([driver.username for driver in obj.driver.all()])
        show_drivers.short_description = 'Motoristas'
    """
