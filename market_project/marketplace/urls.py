# Imports.
from django.urls import path, include

# Import views.
from . import views


# Set your URL patterns here.
app_name = 'marketplace'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('account-details/', views.account_detail_view,
         name='account-details')
]
