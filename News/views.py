from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
import json


def home1(request):
    if request.method == "POST":
        category = request.POST.get("category")

        data = f"https://inshorts-api.herokuapp.com/news?category={str(category)}"

        news = requests.get(data).json()['data']

        with open(f'{category}.json', 'w') as json_file:
            json.dump(news, json_file)

        return redirect(f"/paginator/{category}.json")
    return render(request, "home.html")


def paginator(request, filename):
    with open(filename) as f:
        file = json.load(f)
        paginator = Paginator(file, 4)  # Show 4 contacts per page.

        page_number = request.GET.get('page')
        print(page_number)
        dt = paginator.get_page(page_number)
        # print(dt)

        return render(request, 'home.html', {'dt': dt})
