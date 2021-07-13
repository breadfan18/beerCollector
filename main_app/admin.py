from django.contrib import admin

# Register your models here.
from .models import Beer, Drinking, Award

admin.site.register(Beer)
admin.site.register(Drinking)
admin.site.register(Award)