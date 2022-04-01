
from app import views
from django.urls import path
from app.views import submit
urlpatterns = [
 path('submit/', submit),
 
    
]
