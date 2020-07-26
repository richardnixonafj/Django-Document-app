from django.urls import path
from summa.pessoa import views as v


app_name = 'pessoa'


urlpatterns = [
    path('', v.people_list, name='people_list'),
]