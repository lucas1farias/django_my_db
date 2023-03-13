

"""
Pegar o último objeto de um modelo
Útil p/ algoritmos back-end passados ao front-end do Django, que precisem de inputs p/ enviar novos objetos ao modelo
A versão 1 é uma versão não reciclável que passa atribs. arbitrários na função de acordo com a necessidade
A versão 2 é uma versão reciclável cujo atrib é especificado na parâmetro "atrib" e é maleável de acordo com o modelo
A versão 1 não é JSON, a versão 2 é, portanto suas formas de pegar o objeto são !=
"""


def versao_1():
    """
    * A primeiro versão é menos útil (por não ser reciclável)
    * A função filtra sem base num parâmetro, passando um atrib. arbitrário (aqui: name)
    * A função só serve p/ essa view que usa esse modelo especificamente
    * O modelo (aqui: sel.db) não está em formato JSON

    def __init__(self, **kwargs):
        self.db = Language.objects.all()

        if len(self.db) == 0:
            mock_obj = Language(name='Python')
            mock_obj.save()
        else:
            self.last_object = self.get_last_object_data()

    def get_last_object_data(self) -> str:
        db_size = len(self.db) - 1
        last_object_from_db = None

        for pos, index in enumerate(self.db):
            # Se chegar no último índice do banco, pegar o atributo deste objeto neste índice
            if pos == db_size:
                last_object_from_db = self.db[pos].name

        # Porque usar 'filter'? por lidar com objetos repetidos, enquanto 'get' só lida com um objeto
        # Enquanto 'get' só achar uma ocorrência, seu uso é melhor, mas quando houver objetos repetidos, ele gera erro
        last_input = Language.objects.filter(name=last_object_from_db)

        return last_input[0].name
    """


def versao_2():
    """
    * Esta versão é + útil (pode ser reciclável)
    * A função filtra com base num parâmetro "atrib" (qualquer modelo têm um atrib próprio p/ fazer filtragem)
    * A função serve p/ outras views, sendo o atrib de cada uma usada p/ filtragem é passada p/ "atrib"
    * O modelo (aqui: sel.db_dict) está em formato JSON

    def __init__(self, **kwargs):
        self.db_dict = Language.objects.all().values()

        if len(self.db_dict) == 0:
            mock_obj = Language(name='Python')
            mock_obj.save()
        else:
            self.last_object = self.get_last_object_data(atrib='name')

    def get_last_object_data(self, atrib) -> str:
        db_size = len(self.db_dict) - 1
        last_object_from_db = None

        for pos, index in enumerate(self.db_dict):
            # Se chegar no último índice do banco, pegar o atributo deste objeto neste índice
            if pos == db_size:
                last_object_from_db = self.db_dict[pos][atrib]

        # Porque usar 'filter'? por lidar com objetos repetidos, enquanto 'get' só lida com um objeto
        # Enquanto 'get' só achar uma ocorrência, seu uso é melhor, mas quando houver objetos repetidos, ele gera erro
        last_object = Language.objects.filter(name=last_object_from_db)[0]

        return last_object
    """
