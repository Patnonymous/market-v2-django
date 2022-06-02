from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .models import MarketItem


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class IndexView(ListView):
    template_name = 'marketplace/base_index.html'
    context_object_name = 'featured_item_listings'

    def get_queryset(self):
        return MarketItem.objects.filter(item_is_featured=True).order_by('-item_date_added')
