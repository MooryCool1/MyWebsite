from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.views.decorators.cache import never_cache

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    error = None

    if request.method == 'POST':
        login_type = request.POST.get('login_type', 'username')
        password = request.POST.get('password', '')
        user = None

        if login_type == 'email':
            email = request.POST.get('email', '').strip()
            try:
                found_user = User.objects.get(email=email)
                user = authenticate(request, username=found_user.username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            username = request.POST.get('username', '').strip()
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'User not found'

    context = {'error': error}
    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@never_cache
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)