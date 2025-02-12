from django.shortcuts import render  

def home(request):
    context = {
        'title': 'Welcome to My Blog',
        'message': 'This is a dynamic message from Django!',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            print(f"Received message from {name}: {message}")  # Just printing for now
            return render(request, 'blog/contact_success.html', {'name': name})
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

from .models import Post

def blog(request):
    posts = Post.objects.all()  # Get all blog posts
    return render(request, 'blog/blog.html', {'posts': posts})

from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in after signup
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .forms import ContactForm, SignUpForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')  # Replace 'home' with your desired redirect page
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'blog/login.html', {'form': form})



