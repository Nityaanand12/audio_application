from django.urls import path
from audios.views import home_view, index_view, SaveAudio

urlpatterns = [
    path('', index_view),
    path('record/', home_view),
    path('sample/',SaveAudio.as_view(), name="myurl")
]