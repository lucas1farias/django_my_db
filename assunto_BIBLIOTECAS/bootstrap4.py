

"""
INSTALAÇÃO || pip install django-bootstrap4
SALVAR     || pip freeze > libs.txt
ANEXAR     || pp/settings -> INSTALLED_APPS = ['bootstrap4']

USO NO TEMPLATE (sintaxes mais comuns) (normalmente anexadas ao template base e passado por herança a outros)
  {% load bootstrap4 %}                         [abaixo da tag <!DOCTYPE html>]
  {% bootstrap_css %}                           [abaixo das tags <meta>]
  {% bootstrap_messages %}                      [no topo de <body> ou numa tag estratégica acima de um formulário]
  {% bootstrap_javascript jquery='full'/True %} [antes de </body>]

OBS: "{% bootstrap_messages %}" precisa de outras bibliotecas Django p/ melhor aplicação no template

  -> from django.contrib import messages
  -> (def post)         messages.error(request, 'Mensagem de erro')
  -> (def post)         messages.success(request, 'Mensagem de sucesso')
  -> (def form_valid)   messages.error(self.request, 'Mensagem de erro')
  -> (def form_invalid) messages.success(self.request, 'Mensagem de sucesso')
"""
