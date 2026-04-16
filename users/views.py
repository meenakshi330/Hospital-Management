from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import resend
from django.conf import settings

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            password=password
        )
        resend.api_key = settings.RESEND_API_KEY
        resend.Emails.send(
            {
                'from': 'onboarding@resend.dev',
                'to': ['meenakshi3032003@gmail.com'],
                "subject": 'Welcome to HMS',
                "html": f'<h1>Welcome {user.username}</h1>'
            }
        )
        login(request, user)
        return redirect('/dashboard')
    else:
        return render(request, 'user_signup.html')
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
             login(request, user)
             return redirect('/dashboard')

    return render(request, 'user_login.html')


def user_logout(request):
    logout(request)
    return redirect('/login')

