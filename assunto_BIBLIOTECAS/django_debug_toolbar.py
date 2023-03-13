

def terminal():
    """
    . pip install django-debug-toolbar
    . pip freeze > libs.txt
    """


def settings():
    """
    INSTALLED_APPS = ['debug_toolbar']
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
    """


def urls():
    """
    * "urlpatterns" pode estar configurado normalmente antes do bloco de código abaixo

    from django.conf import settings
    from django.urls import path, include

    if settings.DEBUG:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls))
        ] + urlpatterns
    """
