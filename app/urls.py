from django.urls import path
from .views import home, form_vehiculo, form_mod_vehiculo, modificar_vehiculo, form_del_vehiculo

urlpatterns = [
    path('', home, name='home'),
    path('form_vehiculo', form_vehiculo, name='form_vehiculo'),
    path('modificar_vehiculo', modificar_vehiculo, name='modificar_vehiculo'),
    path('form_mod_vehiculo/<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
    path('form_del_vehiculo/<id>', form_del_vehiculo, name="form_del_vehiculo"),

]
