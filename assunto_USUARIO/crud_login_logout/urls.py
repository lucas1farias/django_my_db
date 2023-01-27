

from django.urls import path  # 1_a
from .views import *  # 1_b

# 1_c
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('sign-up', SignUp.as_view(), name='sign-up'),  # criar conta
    path('sign-out', sign_out, name='sign-out'),        # deslogar da conta
    path('sign-in', SignIn.as_view(), name='sign-in'),  # logar na conta
]
