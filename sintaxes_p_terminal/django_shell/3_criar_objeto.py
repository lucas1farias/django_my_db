

def forma_1():
    """
    * Para criar um objeto, é preciso um modelo criado, validado e migrado, p/ acessá-lo pelo Django Shell
    * O modelo é importado ao shell p/ que seja possível a criação de um objeto via modelo
    * Criar não é o suficiente, é preciso anexar esse objeto ao modelo (função: save())
    * O objeto criado chama um modelo, por conta disso, se a função (save) for usada, fica implícito que é p/ aquele modelo

        python manage.py shell
        from _app.models import *
        new_noun = Nouns(name='dog', translation='cachorro')
        new_noun.save()
"""


def forma_2():
    """
    * O valor do parâmetro passado ainda não existe como objeto no modelo (Chassi)
    * Como a função é "pegar ou criar", se o objeto (var: new) já existir, é capturado, senão, é criado
    * Como é mostrado na última linha, o objeto (var: new) foi add ao modelo (Chassi)
    * Essa função, diferente da exibida na primeira forma, não necessita da função (save()). O salvar é automático

    from app.models import *
    chassis = Chassi.objects.all()
    chassis    -----> <QuerySet [<Chassi: 9BG116GW04C400001>, <Chassi: 9BG116GW04C400002>]>
    new = Chassi.objects.get_or_create(number='9BG116GW04C400003')
    new        -----> (<Chassi: 9BG116GW04C400003>, True)
    chassis    -----> <QuerySet [<Chassi: 9BG116GW04C400001>, <Chassi: 9BG116GW04C400002>, <Chassi: 9BG116GW04C400003>]>
    """
