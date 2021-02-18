# from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home_page_view(request):
    # return HttpResponse("Hello, world!")
    context = {
        'blog_entries': [
            {
                'title': 'Hello, world!',
                'body': 'I have created my first template in Django!'
            },
            {
                'title': 'A title',
                'body': 'And a description.'
            }
        ]
    }
    return render(request, 'pages/index.html', context)


# class AboutView(TemplateView):
#     template_name = "about.html"


def register_view(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            phone_number = form.cleaned_data.get("phone_number")
            user = User.objects.create_user(username, email, password)
            return redirect("login")
    return render(request=request, template_name="pages/register.html", context={"register_form": form})


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("index")
    return render(request=request, template_name="pages/login.html", context={"login_form": form})


def logout_view(request):
    logout(request)
    return redirect("index")
