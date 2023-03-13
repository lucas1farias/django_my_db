

"""
* Mostrar idéias de configuração sobre o que fazer quando modelos forem relacionados e algo precise ser deletado
* Mostrar formas de não deletar objetos criados pelo relacionamento entre modelos, quando algum deles precise ser removido
"""


def forma_1_on_delete_models_set_default():
    """
    * (on_delete) = quando modelos se relacionam, esse tipo de parâmetro DEVE ser configurado
    * A configuração padrão é (models.CASCADE)
    * Isso infere que se um modelo se relaciona a outro e um deles é removido, o outro não têm razão pra existir também
    * Porém, as configurações padrão podem ser mudadas (ex: on_delete=models.SET_DEFAULT, default=1)
    * Acima, infere que caso um modelo seja deletado, dar ao campo dependente um valor "default"
    * Tecnicamente, ao reconfigurar o campo, os objetos vinculados anteriores são salvos devido a nova configuração
    * Tecnicamente, o que está sendo passado é um valor "pk" de um objeto (Assembler)
    * Partindo da premissa de que haja um relacionamento entre (Assembler=criador) e (Vehicle=herdeiro)
    * Os objetos (Assembler) sempre são criados antes de um objeto (Vehicle) então sempre haverá pelo menos 1 objeto
    * Portanto, esse procedimento não deve gerar erros, a não ser que o pk=1 tenha sido deletado e substituído por outro
    * Caso isso aconteça, se deve procurar o (pk) do objeto (Assembler) mais apropriado p/ servir de valor (default)

    class Vehicle(Base):
        # ANTES
        assembler = models.ForeignKey(Assembler, on_delete=models.CASCADE)

        # DEPOIS
        assembler = models.ForeignKey(Assembler, on_delete=models.SET_DEFAULT, default=1)
    """


def forma_2_on_delete_models_set_funcao_customizada():
    """
    * A segunda opção envolve criar uma função que cria um objeto padrão, que carrega um valor temporário
    * "temporário", não significa que será removido, mas que o valor serve como valor de emergência
    * A função se chama (set_default_assembler) e deve ser criada antes do modelo alvo (Vehicle)
    * Caso aconteça de algum modelo com relacionamento seja deletado, os objetos desse relacionamento não serão perdidos
    * Ao invés de ser removido, o campo afetado dos objetos relacionados são reconfigurados e ganham um valor temporário
    * Este valor temporário é o retorno da função programada dentro do campo que cria o relacionamento
    * O retorno possui um índice [0] na chamada, pois seu retorno é uma tupla (o valor que interessa é o índice 0)

    def set_default_assembler():
        return Assembler.objects.get_or_create(name="Padrão")[0]

    class Vehicle(Base):
        ...
        assembler = models.ForeignKey(Assembler, on_delete=models.SET(set_default_assembler))
    """
