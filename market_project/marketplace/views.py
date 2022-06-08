# Imports Django.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

# Imports custom.
from .forms import CustomUserCreationForm
from .models import MarketItem
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


@login_required
def account_detail_view(request):
    """
    Displays basic information about the users account.

    Will be extended to include a link to edit account information.
    """
    return render(request, 'marketplace/base_account_details.html')
