from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, mixins
from shop.models import *
from .premission import *

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Products.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

# class ProductViewSet(mixins.ListModelMixin,
#                      mixins.RetrieveModelMixin,
#                      # mixins.CreateModelMixin,
#                      # mixins.DestroyModelMixin,
#                      viewsets.GenericViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class CountryProivodstvaViewSet(viewsets.ModelViewSet):
    serializer_class = CountryProivodstvaSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = CountryProivodstva.objects.all()
        country = self.request.query_params.get('country', None)

        if country is not None:
            queryset = queryset.filter(country__icontains=country)
        return queryset

class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Brand.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Bill.objects.all()
        name = self.request.query_params.get('clientName', None)
        sur = self.request.query_params.get('clientSurname', None)

        if name is not None:
            queryset = queryset.filter(clientName__icontains=name)
        elif sur is not None:
            queryset = queryset.filter(clientSurname__icontains=sur)
        return queryset

class Pos_orderViewSet(viewsets.ModelViewSet):
    serializer_class = Pos_orderSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Pos_order.objects.all()
        name = self.request.query_params.get('bill', None)

        if name is not None:
            queryset = queryset.filter(bill__icontains=name)
        return queryset
