from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from basket.forms import BasketAddProductForm
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404

def first_view(request):
    return render(request, 'first.html')

def second_view(request):
    return render(request, 'second.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def location_view(request):
    return render(request, 'location.html')



class CategoryListViewMain(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

def cart_view(request):
    return render(request, 'basket/basket_detail.html')

#
#Brand
#

class BrandListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_brand'
    model = Brand
    template_name = 'brand/brand_list.html'
    context_object_name = 'brands'

class BrandDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_brand'
    model = Brand
    template_name = 'brand/brand_detail.html'
    context_object_name = 'brands'

class BrandCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_brand'
    model = Brand
    form_class = BrandForm
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brands_list_view')

class BrandUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_brand'
    model = Brand
    form_class = BrandForm
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brands_list_view')

class BrandDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_brand'
    model = Brand
    context_object_name = 'brands'
    template_name = 'brand/brand_confirm_delete.html'
    success_url = reverse_lazy('brands_list_view')

#
#Category
#

class CategoryListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_category'
    model = Category
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'

class CategoryDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_category'
    model = Category
    template_name = 'categories/categories_detail.html'
    context_object_name = 'categories'

class CategoryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_category'
    model = Category
    form_class = CategoryForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list_view')

class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_category'
    model = Category
    form_class = CategoryForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list_view')

class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.dalete_category'
    model = Category
    context_object_name = 'categories'
    template_name = 'categories/categories_confirm_delete.html'
    success_url = reverse_lazy('categories_list_view')
#
#Country
#

class CountryListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_country'
    model = CountryProivodstva
    template_name = 'countries/countries_list.html'
    context_object_name = 'countries'

class CountryDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_country'
    model = CountryProivodstva
    template_name = 'countries/countries_detail.html'
    context_object_name = 'countries'

class CountryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_country'
    model = CountryProivodstva
    form_class = CountryProivodstvaForm
    template_name = 'countries/countries_form.html'
    success_url = reverse_lazy('countries_list_view')

class CountryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_country'
    model = CountryProivodstva
    form_class = CountryProivodstvaForm
    template_name = 'countries/countries_form.html'
    success_url = reverse_lazy('countries_list_view')

class CountryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_country'
    model = CountryProivodstva
    context_object_name = 'countries'
    template_name = 'countries/countries_confirm_delete.html'
    success_url = reverse_lazy('countries_list_view')

#
#Product
#
class ProductListView_Main(ListView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'productss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context


class ProductListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_product'
    model = Products
    template_name = 'productss/productss_list.html'
    context_object_name = 'productss'


class ProductListViewSort(ListView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'productss'

    def get_queryset(self):
        category_id = self.kwargs.get('category')
        return Products.objects.filter(category__id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs.get('category'))
        context['category'] = category
        context['form_basket'] = BasketAddProductForm()
        return context


class ProductDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_product'
    model = Products
    template_name = 'productss/productss_detail.html'
    context_object_name = 'productss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class ProductDetailViewMain(DetailView):
    model = Products
    template_name = 'product_detail_main.html'
    context_object_name = 'productss'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_product'
    model = Products
    form_class = ProductsForm
    template_name = 'productss/productss_form.html'
    success_url = reverse_lazy('productss_list_view')

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_product'
    model = Products
    form_class = ProductsForm
    template_name = 'productss/productss_form.html'
    success_url = reverse_lazy('productss_list_view')

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_product'
    model = Products
    context_object_name = 'productss'
    template_name = 'productss/productss_confirm_delete.html'
    success_url = reverse_lazy('productss_list_view')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('products_view')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('products_view')
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('products_view')