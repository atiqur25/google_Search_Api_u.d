from django.shortcuts import render, HttpResponse
#  3rd party apps
import requests
from bs4 import BeautifulSoup as bs
import lxml


# pip install requests bs4 lxml


# Create your views here.

def HomepageView(request):
    return render(request, 'google.html')


def Search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = 'https://www.ask.com/web?q=' + search
        # url = 'https://www.google.com/search?q=' + search
        search_stored_variable = requests.get(url)  # this variable store search url
        convert_search_result = bs(search_stored_variable.text, 'lxml')  # convert_search_result using res ,'lxml
        result_list = convert_search_result.find_all('div', {
            'class': 'PartialSearchResults-item'})  # result list form url link
        find_ls = []
        for r in result_list:
            result_title = r.find(class_='PartialSearchResults-item-title').text
            result_url = r.find('a').get('href')
            result_details = r.find(class_='PartialSearchResults-item-details').text

            find_ls.append((result_title, result_url, result_details))

        context = {
            'find_ls': find_ls
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
