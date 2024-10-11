# from django.http import HttpRequest
from django.shortcuts import render


# def index(request):
#     return HttpRequest("Hey hey! home page ) ")


def index(request):
    context = {
        "title": "Zhs Home",
        "content": "Main page of mall - ZhsMall",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "is_authenticated": False,
    }
    return render(request, "main/index.html", context)
