from django.contrib.gis import admin
from models import NigeriaLGA

# Register your models here.
@admin.register(NigeriaLGA)
class NigeriaLGAAdmin(admin.GeoModelAdmin):
	list_display = ['lga','state']
	search_fields = ['name_2','name_1']