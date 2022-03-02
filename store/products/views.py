from django.shortcuts import render


def index(request):
    context = {
        'title': 'La pizza bomba'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'La pizza bomba - Меню'
    }
    return render(request, 'products/products.html', context)


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