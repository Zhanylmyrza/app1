from django.shortcuts import render


def index(request):
    context = {"title": "Home - Главная", "content": "Юхуу🕺 мебельный магазин"}
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас ",
        "content": "Знаем знаем! мы крутыыые 😎",
        "text_on_page": "Целый текс о том, какие мы крутые и в конце чуточку про то, почему этот магазин такой классный, и какой хороший товар :D  ",
    }
    return render(request, "main/about.html", context)
