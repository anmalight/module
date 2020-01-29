from django.contrib import admin
from authentication.models import User
from shop.models import Good, Purchase, Return

# Register your models here.

admin.site.register(User)
admin.site.register(Good)
admin.site.register(Purchase)
admin.site.register(Return)
