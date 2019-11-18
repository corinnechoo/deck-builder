import deck.views
from django.urls import path

from django.contrib import admin
from django.contrib.auth import views as auth_views


admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path("cards/", deck.views.index, name="index"),
]
