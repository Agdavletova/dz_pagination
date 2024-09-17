from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import  csv


def index(request):
    return redirect(reverse('bus_stations'))

CONTENT = {}
def bus_stations(request):

    with open('data-398-2018-08-30.csv', newline='') as f:
        CONTENT = list(csv.DictReader(f))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
         'bus_stations':page.object_list,
         'page':page ,
    }
    return render(request, 'stations/index.html', context)