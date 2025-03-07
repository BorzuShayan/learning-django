from django.urls import path
import website.views as wv

urlpatterns = [
    path('', wv.home),
    path('contact/', wv.contact),
    path('about/', wv.about)
]
