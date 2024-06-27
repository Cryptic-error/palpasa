from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(_("Product Name"), max_length=50)
    desc = models.CharField(max_length=300)
    category=models.CharField(max_length=200)
    price=models.IntegerField()
    prev_price=models.IntegerField()
    image=models.ImageField(upload_to='shop/images')

    def __str__(self) :
        return self.product_name

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')
