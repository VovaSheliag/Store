from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='Nothing to describe')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='images/', blank=True)
    post_date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(blank=True, default=True)
    user = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE, auto_created=True)

    class Meta:
        verbose_name = 'Product'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main_page')


class Cart(models.Model):
    product = models.ForeignKey(Product, related_name='cart', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE,
                             auto_created=True, null=True)

    class Meta:
        verbose_name = 'Cart'

    def __str__(self):
        return f'{self.user} | {self.product.__str__()}'
