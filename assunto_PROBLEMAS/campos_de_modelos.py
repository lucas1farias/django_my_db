

def problema():
    """
    You are trying to add a non-nullable field '' to '' without a default; we can't do that (the database needs
    something to populate existing rows). Please select a fix:

    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit, and let me adda default in models.py
    """


def explicacao():
    """
    * Considere o seguinte contexto:

        Modelos         || Assembler, Chassi, Vehicle
        Relacionamentos || Vehicle possui relacionamento (1 p/ 1) com Chassi
                           Vehicle possui relacionamento (1 p/ muitos) com Assembler

    * O problema descrito acontece por haver objetos (Vehicle) já criados
    * Por exemplo, foi criado um objeto (Vehicle) e DEPOIS, foi adicionado um novo campo neste modelo
    * Os objetos que foram criados ANTES dessa mudança, tornam-se problemáticos, pois este campo novo não existia
    * Por conta disso, na lógica de bancos de dados, campos não podem ser vazios, e estes ficariam
    """


def solucao():
    """
    * O problema desta solução é: tudo feito anteriormente é apagado

    * ETAPA 1 || Remover o banco (Em um projeto Django, o banco padrão é "db.sqlite3")
    * COMANDO || rm db.sqlite3   (O banco se encontra na raiz do projeto)
    * ETAPA 2 || Entrar na pasta da aplicação, onde estão os relatórios das ações do banco deletado
    * COMANDO || cd nome_do_modulo_da_aplicacao
    * ETAPA 3 || Entrar na pasta de migrações
    * COMANDO || cd migrations
    * ETAPA 4 || Remover os módulos que não são "__init__"
    * COMANDO || rm 00* (remove todos os módulos com as inicias especificadas)
    * ETAPA 5 || Descer os 2 níveis subidos, p/ voltar à raiz do projeto
    * COMANDO || cd .. (x2)
    * ETAPA 6 || Refazer os comandos de criação e validação
    * COMANDO || python manage.py makemigrations
    * COMANDO || python manage.py migrate
    * COMANDO || python manage.py createsuperuser (pois, deixa de existir)
    """


def solucao_alternativa():
    """
    * No campo novo que está gerando o problema, add uma das sintaxes reservadas: (blank=True, default='qualquer_valor')
    * O problema dessa solução é que todos os objetos anteriores ao problema, terão o mesmo valor
    * Esse valor pode não ser congruente com o valor real que era desejado ser passado, mas soluciona o problema
    * A opção seria acessar os objetos afetados e editar seus valores manualmente p/ algo desejável
    * COMANDO || python manage.py makemigrations
    * COMANDO || python manage.py migrate
    """
