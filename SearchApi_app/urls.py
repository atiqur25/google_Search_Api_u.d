from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomepageView,name='home'),
]
