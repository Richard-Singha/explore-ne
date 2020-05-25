from django.contrib import admin
from .models import Destination, Image, Festival, Hotspot, Stay, PopularFood 
# Register your models here.

admin.site.register(Destination)
admin.site.register(Image)
admin.site.register(Festival)
admin.site.register(Hotspot)
admin.site.register(Stay)
admin.site.register(PopularFood)