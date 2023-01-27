

"""
* Numa view Django, pelo método __init__, se pode criar algoritmos, e seus resultados são transferíveis ao template
* A transferência se dá pelo método "get_context_data"
* MOTIVO COMUM: Exibir dados das vars no template
* MOTIVO COMUM: Transferir dados das vars ao template p/ ser acessada via JS e ser manipulado
* Normalmente, no segundo motivo, a var fica escondida no template, e a melhor forma de acesso é via classe

    <div class="last-game" style="display: none;">{{ nome_chave_var_contexto }}</div>
"""
