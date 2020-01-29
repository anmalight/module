from django.db import models
from authentication.models import User
from django.utils import timezone
# Create your models here


class Good(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='pic_folder/', blank=True, null=True)
    in_stock = models.PositiveIntegerField()


class Purchase(models.Model):
    info_about_good = models.ForeignKey(Good, on_delete=models.CASCADE)
    info_about_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity_of_goods = models.PositiveIntegerField()
    # quantity_of_goods = models.PositiveIntegerField()
    time_of_purchase = models.DateTimeField(default=timezone.now)


class Return(models.Model):
    info_about_purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    time_of_return = models.DateTimeField(default=timezone.now)
