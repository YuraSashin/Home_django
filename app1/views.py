# from django.shortcuts import render

# Create your views here.

# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html — многострочный текст
# с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

from django.http import HttpResponse, HttpRequest
import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse('Привет мир!')

def index_home(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>home</title>
</head>
<body>
    <h1>Главная</h1>
    <h3>Адрес{request.get_host() + request.path}</h3>
</body>
</html>
    """
    logger.debug('Index page requested.')
    
    return HttpResponse(html)

def about(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>home</title>
</head>
<body>
    <h1>O себе</h1>
    <h3>Адрес {request.get_host()  + request.path}</h3>
    <p>Начинающий программист на Django</p>
</body>
</html>
    """
    logger.debug('About page requested.')

    return HttpResponse(html)