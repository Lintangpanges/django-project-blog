from django.contrib import admin
from .models import*
# Register your models here.

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','kategory','date')

# anjay jadi
# lagi

admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)
