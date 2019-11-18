import deck.views
from django.urls import path

from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path("cards/", deck.views.index, name="index"),
]
