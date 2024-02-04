# from django.shortcuts import render

# Create your views here.

# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html — многострочный текст
# с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

# from django.http import HttpResponse, HttpRequest
# import logging
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Client, Order, Product
# from datetime import datetime, timedelta
# from .forms import ProductForm, ImageForm
# from django.core.files.storage import FileSystemStorage
# from django import forms

# logger = logging.getLogger(__name__)

# def index(request):
#     return HttpResponse('Привет мир!')

# def index_home(request: HttpRequest):
#     html = f"""<!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>home</title>
# </head>
# <body>
#     <h1>Главная</h1>
#     <h3>Адрес{request.get_host() + request.path}</h3>
# </body>
# </html>
#     """
#     logger.debug('Index page requested.')
    
#     return HttpResponse(html)

# def about(request: HttpRequest):
#     html = f"""<!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>home</title>
# </head>
# <body>
#     <h1>O себе</h1>
#     <h3>Адрес {request.get_host()  + request.path}</h3>
#     <p>Начинающий программист на Django</p>
# </body>
# </html>
#     """
#     logger.debug('About page requested.')

#     return HttpResponse(html)

# Продолжаем работать с товарами и заказами.

# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)


# def client_orders(request, client_id):
#     client = Client.objects.get(id=client_id)
#     clients = ['Юра Сашин', 'Петр Петров', 'Игорь Смирнов']
#     orders = Order.objects.filter(client=client)
#     context = {
#         'client': client,
#         'orders': orders
#     }
#     return render(request, 'order_client.html', context)

# def client_products(request, client_id):
#     client = Client.objects.get(id=client_id)
#     client = {'name': 'Юра Сашин'}
#     week_ago = datetime.now() - timedelta(days=7)
#     month_ago = datetime.now() - timedelta(days=30)
#     year_ago = datetime.now() - timedelta(days=365)
#     products = client.order_set.filter(order_date__range=[week_ago, datetime.now()]).values('products__name', 'products__added_date')
#     context = {
#         'client': client,
#         'products_month': client.order_set.filter(order_date__range=[month_ago, datetime.now()]).values('products__name', 'products__added_date'),
#         'products_year': client.order_set.filter(order_date__range=[year_ago, datetime.now()]).values('products__name', 'products__added_date')
#     }
#     return render(request, 'products_client.html', context)


# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.

# def edit_product(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_detail', product_id=product_id)
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'edit_product.html', {'form': form})

# class ImageForm(forms.Form):
#     image = forms.ImageField()

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)
#     else:
#         form = ImageForm()
#     return render(request, 'upload_image.html', {'form': form})