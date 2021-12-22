from django.urls import path

from WebTraining.customer_profile import views
from django.urls import path


from WebTraining.customer_profile.views import customer_profile

urlpatterns = [
    path('', customer_profile, name='customer profile'),
]