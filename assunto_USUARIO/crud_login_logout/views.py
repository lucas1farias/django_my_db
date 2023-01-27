

from django.shortcuts import render

# Index
from django.views.generic import TemplateView

# SignUp
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

# SignOut
from django.contrib.auth import logout

# SignIn
from django.contrib.auth import authenticate
from django.contrib.auth import login


class Index(TemplateView):
    template_name = 'index.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class SignUp(TemplateView):
    template_name = 'sign_up.html'

    def post(self, request):
        msg = {
            'username_already_taken': 'O nome de usuário já existe.',
            'user_email_already_taken': 'Já há uma conta registrada com esse e-mail.',
            'passwords_do_not_match': 'Senha inicial e de confirmação, não são idênticas!',
            'sign-up-successful': '{account_} Seu cadastro foi realizado!'
        }

        conditions = {
            'passwords_are_!=': str(request.POST['password']) != str(request.POST['password_confirm']),
            'username_taken': User.objects.filter(username=request.POST['username']).exists(),
            'email_taken': User.objects.filter(email=request.POST['email']).exists()
        }

        # Se estiver enviando dados
        if str(request.method) == 'POST':

            # Senhas ==
            if conditions['passwords_are_!=']:
                messages.error(request, msg['passwords_do_not_match'])
                return redirect('sign-up')

            # Usuário já existe
            if conditions['username_taken']:
                messages.error(request, msg['username_already_taken'])
                return redirect('sign-up')

            # Email já existe
            if conditions['email_taken']:
                messages.error(request, msg['user_email_already_taken'])
                return redirect('sign-up')

            # Tudo ok
            if True not in tuple(conditions.values()):
                new_user = User.objects.create_user(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                )

                # Como "new_user" é um objeto do modelo "User", o método "save()" o salva como objeto de "User"
                new_user.save()
                messages.success(request, msg['sign-up-successful'].format(account_=new_user.get_full_name()))
                return redirect('index')


def sign_out(request):
    messages.success(request, 'Saída efetuada com sucesso')
    logout(request)
    return redirect('index')


class SignIn(TemplateView):
    template_name = 'sign_in.html'

    def post(self, request):
        msg = {
            'logged_in': 'Login efetuado com sucesso!',
            'incorrect_data': 'Usuário ou senha incorretas'
        }

        if str(request.method) == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Retorno: True ou None
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, msg['logged_in'])
                return redirect('index')
            if not user:
                messages.error(request, msg['incorrect_data'])
                return redirect('sign-in')
