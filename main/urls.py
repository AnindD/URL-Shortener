from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.homepage, name="index"),
    path("url_shortener", views.url_shortener, name="second page"),
    path("homepage", views.homepage, name="homepage"),
    path("terms_and_services", views.terms_and_services, name="terms and services"),
    path("login_page", views.login_page , name="login page"),
    path("signup", views.signup, name="signup"),
    path("aboutme", views.social_media, name="aboutme"),
    path("shortened_link", views.shortened_link, name="shortened_link"),
    path("<int:id>", views.delreq, name="delreq"),
    path("<str:url>", views.redirect_url, name="redirect_url")
]