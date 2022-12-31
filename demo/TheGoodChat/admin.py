from django.contrib import admin
from .models import car
from . import models
# Register your models here.
class carAdmin(admin.ModelAdmin):
    list_display=["name","price","color","descripion","model"]
    list_editable=["price","color"]
    search_fields=["name","price"]
    list_filter=["price","color"]
    #problem --> field=["name","descripion"]
admin.site.register(models.car,carAdmin)
