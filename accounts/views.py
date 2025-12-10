# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Agar Profile modelidan foydalanmasang, forms.py minimal varianti bilan ket.
try:
    from .forms import SignupForm
except Exception:
    SignupForm = None

def signup_view(request):
    if SignupForm is None:
        messages.error(request, "SignupForm topilmadi. accounts/forms.py ni tekshiring.")
        return redirect('accounts:login')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ro‘yxatdan o‘tish muvaffaqiyatli!")
            return redirect('movies:home')
        messages.error(request, "Xatolik: formani to‘g‘ri to‘ldiring.")
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Kirish muvaffaqiyatli!")
            return redirect('movies:home')
        messages.error(request, "Login yoki parol noto‘g‘ri.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Tizimdan chiqdingiz.")
    return redirect('movies:home')

@login_required
def profile_view(request):
    # Minimal profil sahifa — hech qanday qo‘shimcha import yo‘q
    return render(request, 'accounts/profile.html', {})






