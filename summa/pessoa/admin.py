from django.contrib import admin
from summa.pessoa.models import Pessoa_Filiado


@admin.register(Pessoa_Filiado)
class Pessoa_FiliadoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'data_da_extracao',
        'nome_do_partido',
        'nome_do_filiado',
        
    )
    search_fields=('nome_do_filiado',)
    list_filter=('nome_do_partido',)