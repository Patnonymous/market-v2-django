from datetime import datetime
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """
    Extends the AbstractUser.
    Good practice allows for better customization down the line.
    """

    def __str__(self):
        return self.username


class Category(models.Model):
    """
    A category identifier for market items.
    Categories can only be created by the Admins.

    str returns the category name.
    """
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class MarketItem(models.Model):
    """
    Market Items can be posted by all types of users.
    Items can only be set as Featured by Admins.
    Creators can use item_infinite to prevent quantity from changing.

    str returns the item name.
    """
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=7, decimal_places=2, validators=[
                                     MinValueValidator(1)], default=1.00)
    item_quantity = models.PositiveIntegerField(default=1)
    # Controls if an items quantity should be frozen, AKA infinite.
    item_infinite = models.BooleanField(default=False)
    item_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Controls if an item is featured. Featured items show on the index page.
    item_is_featured = models.BooleanField(default=False)
    item_date_added = models.DateTimeField(default=datetime.now)
    # Who posted the item.
    item_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

    def available_for_purchase(self):
        """
        Items with quantity above zero are available for purchase,
        else they are not available.
        """
        if self.item_quantity > 0:
            return True
        else:
            return False

    class Meta:
        verbose_name = 'Market Item'
        verbose_name_plural = 'Market Items'
