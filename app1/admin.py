from django.contrib import admin

# Register your models here.

# Задание
# Настройте под свои нужды вывод информации о клиентах,
# товарах и заказах на страницах вывода информации об объекте и вывода списка объектов.

from django.contrib import admin
from .models import Category, Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'quantity', 'total_price')
    search_fields = ('client__name', 'product__name')
    list_filter = ('product', 'quantity')


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Продукты."""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю, описание продукта(description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Цена',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг',
            {
                'description': 'Рейтинг сформирован на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)