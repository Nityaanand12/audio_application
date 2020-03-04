from django.urls import path
from audios.views import home_view

urlpatterns = [
    path('', home_view)
]