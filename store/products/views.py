from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Добро пожаловать',
        'username': 'Хер с горы',
        'products': [
            {'name': 'Кофта', 'price': 300},
            {'name': 'Штаны', 'price': 400},
            {'name': 'Трусы', 'price': 200},
        ]
    }
    return render(request, 'products/test_context.html', context)