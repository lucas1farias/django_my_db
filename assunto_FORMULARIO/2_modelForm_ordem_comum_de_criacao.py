

"""
models.py, admin.py, terminal, forms.py, views.py, urls.py, template

* Criação do modelo     -> atributos que serão inputs em um formulário modelo que passará os dados p/ este modelo
* Registro do modelo    -> como os dados do modelo se apresentarão no template admin
* Comandos de terminal  -> (makemigrations, migrate)
* Criação do formulário -> formulário em forma de modelo que se conectará ao modelo
* Criação da view       -> recebe o formulário modelo e o modelo e os manipula p/ apresentação no template
* Criação da rota       -> responsável p/ dizer ao Django o endereço da view, que carregará o template
* Criação do template   -> carrega tudo que foi configurado na view (principal: formulário)
"""
