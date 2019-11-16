from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import deck.views

urlpatterns = [
    path("", deck.views.index, name="index"),
]
