from django.shortcuts import render
from .models import Pessoa_Filiado


def people_list(request):
    template_name ='people_list.html'
    objects = Pessoa_Filiado.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)