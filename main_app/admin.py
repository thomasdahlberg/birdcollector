from django.contrib import admin
from .models import Bird, Feeding, Gift

# Register your models here.

admin.site.register(Bird)
admin.site.register(Feeding)
admin.site.register(Gift)

