from django import forms
from shop.models import Good, Purchase, Return


class AddGoodForm(forms.ModelForm):

    class Meta:
        model = Good
        fields = '__all__'


class NewPurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        # fields = ['quantity_of_goods']
        fields = '__all__'


class NewReturnForm(forms.ModelForm):

    class Meta:
        model = Return
        fields = ['info_about_purchase']

