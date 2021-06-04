from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
    if request.method=='POST':
        search=request.POST['search']
        url='https://duckduckgo.com/?q='+search
        #fetching url from duckduckgo.com
        res=requests.get(url)
        #beutifying the text of html
        soup=bs(res.text,'lxml')
        #found the class of the div tag that shows results
        result_listings = soup.find_all('div',{'class':'result results_links_deep highlight_d result--url-above-snippet'})
        #
        final_result = []

        for result in result_listings:
            result_title = result.find(class_ = 'result__title js-result-title').text
            result_url = result.find('a').get('href')
            result_description = result.find(class_ = 'result__snippet js-result-snippet').text
            final_result.append((result_title,result_url,result_description))
            
        context = {
            'final_result': final_result
        }
        return render(request,'search.html',context)
    else :
        return render(request,'search.html')
