from django.db import models

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    disctiption = models.TextField(null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CountryProivodstva(models.Model):
    country = models.CharField(max_length=MAX_LENGTH, verbose_name='Страна производства')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Brand(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название бренда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Products(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование позиции')
    disctiption = models.TextField(null=True, blank=True, verbose_name='Описание')  # Оставляем как есть
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    country = models.ForeignKey(CountryProivodstva, on_delete=models.PROTECT, verbose_name='Страна производства')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд')

    def __str__(self):
        return f"{self.name} - ({self.price} руб.)"

    class Meta:
        verbose_name = 'Сантехника'
        verbose_name_plural = 'Сантехника'


class Bill(models.Model):
    SHOP = 'SH'
    COURIER = 'CR'
    PICKUPPOINT = 'PP'
    TYPE_DELIVERY = [
        (SHOP, 'Самовывоз'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]

    clientName = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя клиента')
    clientSurname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия клиента')
    clientMiddleName = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Отчество клиента')

    items = models.ManyToManyField(Products, through='Pos_order', verbose_name='Товары')

    total_price = models.FloatField(verbose_name='Итоговая цена')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    comment = models.TextField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Комментарий')
    delivery_address = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Тип доставки')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')

    def __str__(self):
        return f"Чек №{self.pk} от {self.create_date.strftime('%d.%m.%Y')}"

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'

class Pos_order(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.PROTECT, verbose_name='Заказ' )
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Товар' )
    count = models.PositiveIntegerField(default=1, verbose_name='Количество' )

    def __str__(self):
        return f'{self.bill.pk} {self.product.name} ({self.bill.clientName} {self.bill.clientSurname})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
