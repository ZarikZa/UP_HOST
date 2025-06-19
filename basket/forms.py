from django import forms
from shop.models import Bill

class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(min_value=1, max_value=30, initial=1, label="Количетсво",
                               widget=forms.NumberInput(attrs={'class': "form-control"}))
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = (
            'clientName',
            'clientSurname',
            'clientMiddleName',
            'comment',
            'delivery_address',
            'delivery_type',
        )
        widgets = {
            'clientName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя клиента',
            }),
            'clientSurname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию клиента',
            }),
            'clientMiddleName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество клиента (необязательно)',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий к заказу',
                'rows': 3,
            }),
            'delivery_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес доставки',
            }),
            'delivery_type': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
