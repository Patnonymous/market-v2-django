# Imports.
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Category, CustomUser, MarketItem


# Create custom forms here.
# Account related forms section.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    """
    CustomUserChangeForm for changing user details on the admin page.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class EditAccountDetailsForm(forms.ModelForm):
    email = forms.EmailField(label='New Email', required=True)
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


# Category forms section.
class AddNewCategoryForm(forms.ModelForm):
    category_name = forms.CharField(label='Category Name', required=True)

    class Meta:
        model = Category
        fields = ('category_name',)


# Item forms section.
class AddNewItemForm(forms.ModelForm):
    item_name = forms.CharField(label='Item Name', required=True)
    item_description = forms.CharField(
        label='Item Description', max_length=200, required=True)
    item_price = forms.DecimalField(
        label='Price Per Unit', max_digits=7, decimal_places=2, min_value=1, required=True, initial=1.00)
    item_quantity = forms.IntegerField(
        label='Quantity', min_value=1, required=True, initial=1)
    item_infinite = forms.BooleanField(
        label='Freeze Item Quantity', required=False, initial=False)
    item_category_id = forms.ModelChoiceField(
        queryset=Category.objects, label='Category', required=True)
    item_is_featured = forms.BooleanField(
        label='Featured Item', required=False, initial=False)

    class Meta:
        model = MarketItem
        fields = ('item_name', 'item_description', 'item_price', 'item_quantity',
                  'item_infinite', 'item_category_id', 'item_is_featured')
