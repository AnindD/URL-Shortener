import pyshorteners
import random 
import string
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .forms import RegisterForm
from .models import Shortened_URL

def home(request):
    return render(request, "main/base.html", {"name": "Joseph"})

def url_shortener(response): 
    # Context{} has two ShortURLs. One for anonymous users and another for authenticated users. 
    random_characters = ""
    characters = list(string.ascii_letters) + list(string.digits)
    template = loader.get_template('main/shortener.html')
    linked = False 
    if response.method == "POST" and response.user.is_authenticated:
        try: 
            linked = True 
            url = response.POST.get("link")
            for x in range(6): 
                random_characters += random.choice(characters)
            # Filtering to see if it is a unique URL address as we do not want duplicate URLs. 
            while len(Shortened_URL.objects.filter(short_url=random_characters)) !=0:
                for x in range(6): 
                    random_characters += random.choice(characters)
            response.user.URL_user_main.create(original_url=url, short_url=random_characters)
            context = {"linked": linked, "ShortURL2": random_characters}
            return HttpResponse(template.render(context, response))
        except Exception as e: 
            print(e)
    else: 
        try:
            # Pyshortener will be used here as creating individual URLs for anonymous users will require another model without a foreign key. 
            linked = True 
            print("No user is logged in") 
            url = response.POST.get("link")
            shortened_url = pyshorteners.Shortener().tinyurl.short(url)
            context = {"ShortURL": shortened_url, "linked": linked}
            return HttpResponse(template.render(context, response))
        except Exception as e: 
            print(e)
    context = {}
    return render(response, "main/shortener.html", context)


def shortened_link(response):
    link = Shortened_URL.objects.all(); 
    context = {"link": link}
    return render(response, "main/shortened_link.html", context)

def delreq(response, id):
    linkObject = Shortened_URL.objects.get(id=id)
    linkObject.delete()
    link = Shortened_URL.objects.all() 
    context = {"link": link}
    if response.method == "POST":
        print("POST REQUEST")
    return render(response, "main/shortened_link.html", context)

# Temporary page acting as a gateway to your real URL and shortened URL. 
def redirect_url(response, url):
    current_url_object = Shortened_URL.objects.filter(short_url=url)
    if len(current_url_object) == 0: 
        return render(response, "main/homepage.html")
    context = {"obj" : current_url_object[0]}  
    return render(response, "main/redirect_url.html", context)
 

def homepage(request):
    return render(request, "main/homepage.html")

def terms_and_services(request): 
    return render(request, "main/terms_and_services.html")

def login_page(response): 
    if response.method == "POST":
        login_username = response.POST.get("login_username")
        login_password = response.POST.get("login_password")

        user = authenticate(response, username=login_username, password=login_password)
        
        if user is not None:
            print("User does exist!")
            login(response, user)
            redirect("/shortener")
        else:
            print("User does not exist")
    context = {}
    return render(response, "main/login_page.html", context)

def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)  
        if form.is_valid(): 
            form.save()
        return redirect("/login_page")
    else:
        form = RegisterForm(); 
    context = {"form": form}
    return render(response, "main/signup.html", context)


def social_media(request):
    return render(request, "main/aboutme.html")
 

