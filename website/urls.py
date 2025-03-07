from django.urls import path
from website.views import home, json

urlpatterns = [
    path('', home),
    path('json/', json)
]
