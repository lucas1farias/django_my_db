

"""
* Os dados são acessados dentro de "form_valid" via "form"
* Esse contexto é apropriado somente p/ consultar dados via terminal
* Se for tentado exibir esse dado via uma "var self" em "__init__", ele não é exibível no template
* Exemplo:
* (Em __init__)         self.data = ''
* (Em form_valid)       self.data = form.cleaned_data.get('input_atrib_name')
* (Em get_context_data) context['data'] = self.data
* O dado instanciado em "form_valid" são exibíveis no terminal após a submissão, mas não é passada ao template

def form_valid(self, form):
    print(dir(form))
    print('--->', form.cleaned_data.get('nome_do_valor_do_atrib_name_no_input_alvo'))
    form.save()
    messages.success(self.request, 'Mensagem de sucesso')
    return super(LanguageFormView, self).form_valid(form)
"""
