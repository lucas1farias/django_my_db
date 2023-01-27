

"""
* Cria um bloco de código, que vêm de um template inicial e que se repete num template herdeiro
* Quando instanciado no template inicial, esse bloco estará vazio, pois o conteúdo é inserido no template herdeiro
* Quando instanciado no template herdeiro, esse bloco recebe o conteúdo pertinente
* O nome do bloco passado no inicial, deve ser identico no template herdeiro
* EX: TEMPLATE INICIAL: {% block css %} {% endblock %}    TEMPLATE HERDEIRO: {% block css %} Conteúdo {% endblock %}
* Todo bloco aberto {% block nome_do_bloco %}, deve ser fechado {% endblock %}

{% block nome_do_bloco %} {% endblock %}
"""
