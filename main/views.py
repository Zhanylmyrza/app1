from django.shortcuts import render

from goods.models import Category


def index(request):

    categories = Category.objects.all()

    context = {
        "title": "Home - Главная",
        "content": "Юхуу🕺 мебельный магазин",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас ",
        "content": "Знаем знаем! мы крутыыые 😎",
        "text_on_page": "Целый текс о том, какие мы крутые и в конце чуточку про то, почему этот магазин такой классный, и какой хороший товар :D  ",
    }
    return render(request, "main/about.html", context)
