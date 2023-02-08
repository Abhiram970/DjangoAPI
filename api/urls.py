from django.urls import path 
from . import views
urlpatterns = [
    path('langTranslate/',views.langTranslate) 
]
