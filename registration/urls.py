from django.urls import path
from registration import views


urlpatterns = [
    path('', views.list_user, name='home'),
    path('form/',views.registration_form, name='form'),

]
