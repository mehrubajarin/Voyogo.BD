from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.


def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomAuthenticationForm()

    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


def logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("/")


@login_required
def profile(request):
    from travello.models import Purchase

    travel_history = []
    if request.user.is_authenticated:
        travel_history = (
            Purchase.objects.filter(user=request.user)
            .select_related("package")
            .order_by("-purchased_at")
        )
    return render(request, "profile.html", {"travel_history": travel_history})


@login_required
def travel_history(request):
    from travello.models import Purchase

    purchases = (
        Purchase.objects.filter(user=request.user)
        .select_related("package")
        .order_by("-purchased_at")
    )

    return render(request, "travelhistory.html", {"purchases": purchases})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def news(request):
    return render(request, "news.html")


def destinations(request):
    return render(request, "destinations.html")
