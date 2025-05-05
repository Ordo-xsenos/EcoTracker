from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import login,registration,get_discord_members

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("registration/", registration, name="registration"),
    path('discord/members/', get_discord_members, name='discord_members'),
]
