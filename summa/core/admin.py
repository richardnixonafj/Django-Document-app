from django.contrib import admin
from .models import Filiado

@admin.register(Filiado)
class FiliadoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'data_da_extracao',
        'nome_do_partido',
        'nome_do_filiado',
        
    )
    search_fields=('nome_do_filiado',)
    list_filter=('nome_do_partido',)
