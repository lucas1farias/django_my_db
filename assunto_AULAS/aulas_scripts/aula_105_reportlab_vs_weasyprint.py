

"""
Módulo: aula_105_reportlab_vs_weasyprint.py
"""

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 12:Adicionando outras funcionalidades
    Aula:   # 105. Precisa gerar PDF na sua aplicação Django? Vamos lá!
    """

def browser():
    """
    Pesquisa  # Reportlab
    Website   # https://www.reportlab.com/dev/docs/
    """

def terminal():
    """
    pip install django
    pip install reportlab
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    from os import path
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = ['pa']
    TEMPLATES = [{'DIRS': ['templates']}]
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'media')
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('', IndexView.as_view(), name='index'),
        path('download/pdf/report-lab', ReportLabView.as_view(), name='download/pdf/report-lab'),
        path('download/pdf/report-lab/1', ReportLabDownloadView.as_view(), name='download/pdf/report-lab/1')
    ]
    """

# as_attatchment=False / removido -> não abrir o módulo como pop-up no template, mas abrir na página
def views():
    """
    from django.http import FileResponse
    from django.shortcuts import render
    from django.views.generic import View
    from reportlab.pdfgen import canvas
    import io

    class IndexView(View):
        def get(self, request, *args, **kwargs):
            context = {'title': 'Página Índice'}
            return render(request, 'index.html', context)

    class ReportLabView(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'reportlab.html')

    class ReportLabDownloadView(View):

        def get(self, request, *args, **kwargs):
            buffer = io.BytesIO()
            pdf = canvas.Canvas(buffer)

            pdf.drawString(10, 10, 'Obrigado, por baixar o arquivo')
            pdf.drawString(10, 50, ':D')
            pdf.showPage()
            pdf.save()
            buffer.seek(0)

            # as_attatchment=False / removido -> não abrir o módulo como pop-up no template, mas abrir na página
            return FileResponse(buffer, as_attachment=True, filename='texto.pdf')
    """

# Irrelevante para o contexto da aula, criado apenas para não abrir na página padrão Django
def templates_index():
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link
            crossorigin="anonymous"
            href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
            rel="stylesheet"
        >
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
    </head>
    <body>
        <h2 class="text-primary">{{ title }}</h2>
        <script
            crossorigin="anonymous"
            integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
            src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        ></script>

        <script
            crossorigin="anonymous"
            integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
            src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
        ></script>
    </body>
    </html>
    """

# Nome: reportlab.html
"O download é gerado na view, que nesse contexto é [ ReportLabDownloadView ]"
"Não há a necessidade de criar o template, apenas a rota, seguido da view"
def templates():
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link
            crossorigin="anonymous"
            href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
            rel="stylesheet"
        >
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
    </head>
    <body>
        <div class="container text-center mt-2">
            <h2 class="text-secondary">Baixar módulo .pdf usando ReportLab</h2>
            <a class="btn btn-danger text-warning" href="{% url 'download/pdf/report-lab/1/' %}">Download</a>
        </div>
        <script
            crossorigin="anonymous"
            integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
            src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        ></script>

        <script
            crossorigin="anonymous"
            integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
            src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
        ></script>
    </body>
    </html>
    """

def terminal2():
    """
    python manage.py migrate
    python manage.py runserver
    """

"Testar a rota http://127.0.0.1:8000/download/pdf/report-lab/ fazendo o download"
"Se der certo, a rota http://127.0.0.1:8000/download/pdf/report-lab/1/ será carregada com o download do pdf"
#######################################################################################################################

def browser2():
    """
    Pesquisa  # weasyprint
    Website   # https://weasyprint.org/
    """

def terminal3():
    """
    pip install WeasyPrint
    pip freeze > requirements.txt
    """

def pa_urls2():
    """
    url patterns = [
        path('download/pdf2/weasyprint/', WeasyPrintView.as_view(), name='download/pdf2/weasyprint/'),
        path('download/pdf2/weasyprint/1/', WeasyPrintDownloadView.as_view(), name='download/pdf2/weasyprint/1/')
    ]
    """

"Na lista de conteúdos [ data ], colocam-se os dados que farão parte do módulo pdf a ser baixado"
""" 'attatchment: filename="weasyprint.pdf"' = Faz o download do módulo .pdf """
""" 'inline: filename="weasyprint.pdf"'      = Abre o módulo .pdf na própria página (se o navegador possui plugin) """
def views2():
    """
    class WeasyPrintView(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'weasyprint.html')

    class WeasyPrintView(View):

        def get(self, request, *args, **kwargs):
            data = ['Lucas Farias Santos de Sousa', 'Estudante backend Python e Django', 'Estudante HTML5 & CSS3']

            html_string = render_to_string('weasyprint.html', {'data': data})
            html = HTML(string=html_string)
            html.write_pdf(target='/tmp/weasyprint.pdf')
            fs = FileSystemStorage('/tmp/')

            with fs.open('weasyprint.pdf') as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attatchment: filename="weasyprint.pdf"'
                return response
    """

# Nome: weasyprint.html
def templates2():
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link
            crossorigin="anonymous"
            href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
            rel="stylesheet"
        >
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Download pdf pelo weasyprint</title>
    </head>
    <body style="background-color: #222;">
        <div class="container text-center mt-3">
            <h2 class="text-primary mb-3">Baixar módulo .pdf pelo Weasyprint?</h2>
            <a class="btn btn-dark text-danger" href="{% url 'download/pdf2/weasyprint/1/' %}">Download</a>
        </div>
        <script
            crossorigin="anonymous"
            integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
            src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        ></script>

        <script
            crossorigin="anonymous"
            integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
            src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
        ></script>
    </body>
    </html>
    """

# Nome: weasyprint-download.html
def templates3():
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link
            crossorigin="anonymous"
            href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
            rel="stylesheet"
        >
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Download - Weasyprint</title>
    </head>
    <body style="background-color: #222;">
        <h2 class="text-danger text-center mb-3">Dados coletados</h2>
        <div class="container text-primary text-right mb-3">{{ data.0 }}</div>
        <div class="container text-primary text-center mb-3">{{ data.1 }}</div>
        <div class="container text-primary text-left mb-3">{{ data.2 }}</div>
        <script
            crossorigin="anonymous"
            integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
            src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        ></script>

        <script
            crossorigin="anonymous"
            integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
            src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
        ></script>
    </body>
    </html>
    """

def terminal4():
    """ python manage.py runserver """

"Testar a rota http://127.0.0.1:8000/download/pdf2/weasyprint/ fazendo o download"
"Se der certo, a rota http://127.0.0.1:8000/download/pdf2/weasyprint/1/ será carregada com o download do pdf"

# ReportLab
"Usou 1 template para exibir o download, o conteúdo do download foi feito em [ views ]"
"Pode reduzir os códigos escritos, mas para mellhor customização, é preciso conhecer a documentação do ReportLab"

# WeasyPrint
"Usou 2 templates, um para exibir o download, outro pra exibir o conteúdo do download"
"O conteúdo do download foi feito no segundo template, o que torna melhor, a customização"
