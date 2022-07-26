# Imports.
from django.urls import path, include

# Import views.
from . import views


# Set your URL patterns here.
app_name = 'marketplace'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('listings/', views.UserListingsView.as_view(), name='user-listings'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('account-details/', views.account_detail_view, name='account-details'),
    path('change-password/', views.ChangePasswordView.as_view(),
         name='change-password'),
    path('edit-account', views.change_account_details, name='edit-account'),
    path('category-management', views.CategoryManagementListView.as_view(),
         name='category-management'),
    path('category-add', views.AddCategoryFormView.as_view(), name='category-add'),
    path('category-delete/<int:pk>', views.delete_category, name='category-delete'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(),
         name='category-detail'),
    path('item-management', views.MarketItemManagementListView.as_view(),
         name='item-management'),
    path('item-add', views.AddMarketItemFormView.as_view(), name='item-add'),
    path('item-delete/<int:pk>', views.delete_item, name='item-delete'),
    path('item/<int:pk>', views.MarketItemDetailView.as_view(), name='item-detail'),
]
