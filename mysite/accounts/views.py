from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную страницу


User = get_user_model()


@user_passes_test(lambda u: u.is_superuser, login_url='/login/')
def admin_panel(request):
    query = request.GET.get('q', '')  # Получаем поисковый запрос
    users_list = User.objects.all()

    if query:
        users_list = users_list.filter(username__icontains=query)  # Фильтруем по имени

    # Пагинация
    paginator = Paginator(users_list, 10)  # 10 пользователей на странице
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)

    return render(request, 'accounts/admin_panel.html', {'users': users})