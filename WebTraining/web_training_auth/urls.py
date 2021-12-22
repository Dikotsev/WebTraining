from django.urls import path



from WebTraining.web_training_auth.views import sign_up, sign_out, sign_in

urlpatterns = [
    path('sign_in/', sign_in, name='sign in'),
    path('sign_out/' ,sign_out, name='sign out'),
    path('sign_up/', sign_up, name='sign up'),
]