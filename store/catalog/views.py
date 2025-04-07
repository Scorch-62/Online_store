from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def catalog(request):
    return render(request, 'catalog.html')


def category(request):
    return render(request, 'category.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Сообщение отправлено {name}({email}): {message}')
    return render(request, 'contacts.html')
