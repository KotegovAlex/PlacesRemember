from django.urls import path

from .views import (
    AddPlace,
    Home,
    LoginUser,
    RegisterUser,
    ShowPlace,
    about,
    logout_user,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about/", about, name="about"),
    path("add_place/", AddPlace.as_view(), name="add_place"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("place/<int:place_id>/", ShowPlace.as_view(), name="place"),
]
