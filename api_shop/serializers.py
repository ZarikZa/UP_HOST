from rest_framework import serializers
from shop.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'disctiption',
            'photo'
        ]

class CountryProivodstvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryProivodstva
        fields = [
            'country',
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
        ]
class ProductsSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Products
        fields = [
            'name',
            'disctiption',
            'price',
            'photo',
            'create_date',
            'category',
            'country',
            'brand',
        ]


class BillSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(label='цена', max_digits=10, decimal_places=2)

    class Meta:
        model = Bill
        fields = [
            'clientName',
            'clientSurname',
            'clientMiddleName',
            'items',
            'total_price',
            'create_date',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_finish',
        ]

class Pos_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'bill',
            'product',
            'count',
        ]

