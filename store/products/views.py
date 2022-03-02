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

