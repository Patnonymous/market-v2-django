# Imports Django.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

# Imports custom.
from .forms import AddNewCategoryForm, AddNewItemForm, CustomUserCreationForm, EditAccountDetailsForm, AddNewItemImageForm
from .models import MarketItem, Category, ItemImage
User = get_user_model()


# Create your views here.
class SignUpView(CreateView):
    """
    SignUpView contains form for new account creation.
    Extends CreateView and UserCreationForm, supports error messages and redirect
    out of the box.

    Rather ugly right now.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ChangePasswordView(PasswordChangeView):
    """
    ChangePasswordView contains a form for the current user to change their password.
    Extends PasswordChangeView, supports error messages and redirect out of the box.

    Also ugly right now. Should be extended with a custom form later.
    """
    template_name = 'marketplace/base_change_password.html'
    success_url = reverse_lazy('marketplace:account-details')


class IndexView(ListView):
    """
    IndexView extends ListView and will display Featured market items.

    The class may have to be extended and edited later.
    """
    template_name = 'marketplace/base_index.html'
    context_object_name = 'featured_item_listings'

    print('Hello world. IndexView.')

    def dispatch(self, request, *args, **kwargs):
        print(request.user.get_user_permissions())
        return super(ListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return MarketItem.objects.filter(item_is_featured=True).order_by('-item_date_added')


class UserListingsView(ListView):
    template_name = 'marketplace/base_user_listings.html'
    context_object_name = 'item_listings'

    def get_queryset(self):
        return MarketItem.objects.filter(item_is_featured=False).order_by('-item_date_added')


# Category views section.
class CategoryManagementListView(ListView):
    model = Category
    template_name = 'marketplace/base_category_management.html'
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddCategoryFormView(FormView):
    """
    Displays a form with relevant inputs to add a new category.
    """
    template_name = 'marketplace/base_category_add.html'
    form_class = AddNewCategoryForm
    success_url = reverse_lazy('marketplace:category-management')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


def delete_category(request, pk):
    category_to_delete = Category.objects.get(id=pk)
    category_to_delete.delete()
    return redirect('marketplace:category-management')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'marketplace/base_category_detail.html'


# Market item views section.
class MarketItemManagementListView(ListView):
    model = MarketItem
    template_name = 'marketplace/base_item_management.html'
    context_object_name = 'item_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddMarketItemFormView(FormView):
    template_name = 'marketplace/base_item_add.html'
    form_class = AddNewItemForm
    success_url = reverse_lazy('marketplace:item-management')

    def form_valid(self, form):
        form.instance.item_owner = self.request.user
        form.save()
        return super().form_valid(form)


class MarketItemDetailView(DetailView):
    model = MarketItem
    template_name = 'marketplace/base_item_detail.html'


class ItemImageManagementListView(ListView):
    model = ItemImage
    template_name = 'marketplace/base_item_image_management.html'
    context_object_name = 'image_list'


class AddItemImageFormView(FormView):
    template_name = 'marketplace/base_item_image_add.html'
    form_class = AddNewItemImageForm
    success_url = reverse_lazy('marketplace:item-image-management')

    def form_valid(self, form):
        print('\nform_valid')
        form.save()
        return super().form_valid(form)


def delete_item(request, pk):
    item_to_delete = MarketItem.objects.get(id=pk)
    item_to_delete.delete()
    return redirect('marketplace:item-management')


def delete_image(request, pk):
    image_to_delete = ItemImage.objects.get(id=pk)
    image_to_delete.delete()
    return redirect('marketplace:item-image-management')


# Account details views section.
def change_account_details(request):
    """
    View displays a form for editing the current users information.

    Since an instance is supplied, form.save() will update said Model instance instead of creating a new one.
    """
    form = EditAccountDetailsForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('marketplace:account-details')
    return render(request, 'marketplace/base_change_account_details.html', {'edit_account_form': form})


@login_required
def account_detail_view(request):
    """
    Displays basic information about the users account.

    Will be extended to include a link to edit account information.
    """
    return render(request, 'marketplace/base_account_details.html')
