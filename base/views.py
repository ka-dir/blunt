from django.shortcuts import render
import requests

# Create your views here.
API_KEY = 'caf2685b4cdd4c31803d6b9510901712'


def home_page(request):
    country = request.GET.get('country') if request.GET.get('country') != None else 'us'
    category = request.GET.get('category') if request.GET.get('category') != None else 'general'
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        res = requests.get(url)
        data = res.json()
        articles = data['articles'][:3]
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        res = requests.get(url)
        data = res.json()
        articles = data['articles'][:3]
    context = {'articles': articles}
    return render(request, 'base/home.html.twig', context)







