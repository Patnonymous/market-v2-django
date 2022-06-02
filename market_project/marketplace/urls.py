# Imports.
from django.urls import path

# Import views.
from . import views


# Set your URL patterns here.
app_name = 'marketplace'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
