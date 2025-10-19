from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("profile", views.profile, name="profile"),
    path("travel-history", views.travel_history, name="travel-history"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("news", views.news, name="news"),
    path("destinations", views.destinations, name="destinations"),
]
