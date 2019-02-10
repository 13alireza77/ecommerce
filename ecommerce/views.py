from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import contactForm, LoginForm, registerForm
from django.contrib.auth import login, authenticate, get_user_model


def homePage(request):
    context = {
        "title": "Home Page",
        "content": "welcome to the home page.",
    }
    return render(request, "homePage.html", context)


def aboutPage(request):
    context = {
        "title": "About Page",
        "content": "welcome to the about page.",
    }
    return render(request, "homePage.html", context)


def contactPage(request):
    cf = contactForm(request.POST or None)
    context = {
        "title": "content Page",
        "content": "welcome to the contact page.",
        "form": cf,
    }
    if cf.is_valid():
        print(cf.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('full name'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def loginPage(request):
    lf = LoginForm(request.POST or None)
    context = {
        "form": lf
    }
    print(request.user.is_authenticated)
    if lf.is_valid():
        print(lf.cleaned_data)
        username = lf.cleaned_data.get("username")
        password = lf.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("Error")
    return render(request, "auth/login.html", context)


User = get_user_model()


def registerPge(request):
    lr = registerForm(request.POST or None)
    context = {
        "form": lr
    }
    if lr.is_valid():
        username = lr.cleaned_data.get("username")
        password = lr.cleaned_data.get("password1")
        email = lr.cleaned_data.get("email")
        newUser = User.objects.create_user(username, email, password)
        print(newUser)
        print(lr.cleaned_data)
    return render(request, "auth/register.html", context)
