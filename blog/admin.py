from django.contrib import admin

# Register your models here.
from .models import Equipement
from .models import Animal

admin.site.register(Equipement)
admin.site.register(Animal)