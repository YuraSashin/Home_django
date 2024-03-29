from django.db import models

# Create your models here.

# Создайте три модели Django: клиент, товар и заказ. Клиент
# может иметь несколько заказов. Заказ может содержать
# несколько товаров. Товар может входить в несколько
# заказов.


# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
class Client(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        # return f'{self.name}, email: {self.email}, register date: {self.register_date}'
        return self.name

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
class Product(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()

    def __str__(self) -> str:
        # return f'{self.title}, price: {self.price}, count: {self.count}'
        return self.name

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
class Order(models.Model):
    objects = None
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_sum = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        # return f'{self.client.name} ordered {self.product} = {self.order_sum}, order date: {self.order_date}'
        return f"Order #{self.id}"

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name