from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='technopost-home'),
    path('about/',views.about,name='technopost-about'),
]
