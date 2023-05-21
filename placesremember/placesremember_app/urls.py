from django.urls import path

from .views import AddPlace, AuthUserPlaces, LoginUser, RegisterUser, ShowPlace, \
    about, index, logout_user

urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name='about'),
    path("places/", AuthUserPlaces.as_view(), name='places'),
    path("add_place/", AddPlace.as_view(), name='add_place'),
    path("login/", LoginUser.as_view(), name='login'),
    path("logout/", logout_user, name='logout'),
    path("register/", RegisterUser.as_view(), name='register'),
    path("place/<int:place_id>/", ShowPlace.as_view(), name='place'),
]
