

"""
* Sintaxe baseada em "class based views" mais comuns p/ usuário, que podem ser passadas p/ "get_context_data"
* Essas sintaxes podem ser passadas diretamente no template sem "self"

self.request.user
self.request.user.is_anonymous
self.request.user.first_name
self.request.user.last_name
self.request.user.username
self.request.user.email
self.request.user.last_login
self.request.user.password
"""
