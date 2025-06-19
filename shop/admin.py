from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(CountryProivodstva)
class CountryProivodstvaAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    pass
@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    pass
