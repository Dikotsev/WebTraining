

from WebTraining.properties.views import index,update_property,add_property,show_properties
from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', index ,name='index'),
    path('show/', show_properties, name='show properties'),
    path('update/<int>pk', update_property, name='update property'),
    path('add/',add_property, name='add property')

]