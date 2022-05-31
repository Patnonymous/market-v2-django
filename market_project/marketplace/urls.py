# Imports.
from django.urls import path


from .views import SignUpView


# Set your URL patterns here.
app_name = 'marketplace'
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
