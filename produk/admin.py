from django.contrib import admin
from .models import Brand, Aksesoris, Apparel, Sepeda, Sparepart

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
	list_display = ['__str__',	'deskripsi', 'tgl_input']
	list_filter = ['tgl_input']

class SepedaAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'kategori', 'subkategori', 'tgl_input']
	list_filter = ['tgl_input']

admin.site.register(Brand, BrandAdmin)
admin.site.register(Aksesoris)
admin.site.register(Apparel)
admin.site.register(Sepeda, SepedaAdmin)
admin.site.register(Sparepart)