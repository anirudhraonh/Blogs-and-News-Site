from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
import requests

from blogs.forms import searchForm
#newsapi
from newsapi.newsapi_client import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='86a49b33733d4c4298db54ce0c0d87ea')

from datetime import datetime, timedelta

# Calculate the date range for the past 30 days
to_date = datetime.now()
from_date = to_date - timedelta(days=30)

# /v2/everything
all_articles = newsapi.get_everything(q='war',
                                    sources="times-now,quint, abc-news,al-jazeera-english,ars-technica,associated-press,axios,bbc-news,bbc-sport,bleacher-report,bloomberg,business-insider,cbs-news,cnn,crypto-coins-news,engadget,entertainment-weekly,espn,ESPN,fortune,fox-news,fox-sports,google-news,hacker-news,ign,independent,mashable,medical-news-today,msnbc,national-geographic,new-scientist,newsweek,new-york-magazine,nfl-news,nhl-news,politico,recode,reddit-r-all,reuters,salon,techcrunch,techradar,the-economist,the-hill,the-huffington-post,the-new-york-times,the-verge,the-wall-street-journal,the-washington-post,time,usa-today,vice-news,wired",
                                    domains='bbc.co.uk,techcrunch.com',
                                    from_param=from_date.strftime('%Y-%m-%d'),
                                    to=to_date.strftime('%Y-%m-%d'),
                                    language='en',
                                    sort_by='relevancy',
                                    page=2)
# Create your views here.
def home(request):
    return render(request,'main/base.html')

def news(request):
    #searchbar
    form=searchForm()
    if request.method == 'POST' and form.is_valid:
        form = searchForm(request.POST or None)
        form.save(commit=False)
        query = form.cleaned_data['query']
        #api endpoint
        url = f" https://newsapi.org/v2/everything?q={query}&apiKey=86a49b33733d4c4298db54ce0c0d87ea"
        response = requests.get(url).json()
        matching_articles = response.get('articles',[])

        return render(request,'main/news.html',{'matching_articles':matching_articles})
    return render(request,'main/news.html',{'all_articles':all_articles})

def reg(request):
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        print('--------')
        print(form)
        if form.is_valid():
            form.save()
            return redirect('main:Login')
        else:
            errors = form.error_messages 
            return render(request,'main/reg.html',{'errors' :errors})

    else:
        form = UserCreationForm()
        return render(request,'main/reg.html',{'form':form})
    
def logout_page(request):
    logout(request)
    return redirect('blogs:BlogsPage')
    