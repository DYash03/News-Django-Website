from django.shortcuts import render
from django.http import HttpResponse
from . models import New, Sport, Video, Tv, Weather, Contact
from django.db.models import Q
from itertools import chain
from news_app.templatetags import class_name
# Create your views here.


def home(request):
    breaking = New.objects.all().filter(
        Type="Breaking").order_by('-news_id')[:5][::-1]
    india = New.objects.all().filter(
        ~Q(Type="Breaking"), category="India").order_by('-news_id')[:4][::-1]
    world = New.objects.all().filter(
        ~Q(Type="Breaking"), category="World").order_by('-news_id')[:4][::-1]
    election = New.objects.all().filter(
        ~Q(Type="Breaking"), category="Election").order_by('-news_id')[:4][::-1]
    business = New.objects.all().filter(
        ~Q(Type="Breaking"), category="Business").order_by('-news_id')[:4][::-1]
    tech = New.objects.all().filter(
        ~Q(Type="Breaking"), category="Tech").order_by('-news_id')[:4][::-1]
    science = New.objects.all().filter(
        ~Q(Type="Breaking"), category="Science").order_by('-news_id')[:4][::-1]
    health = New.objects.all().filter(
        ~Q(Type="Breaking"), category="Health").order_by('-news_id')[:4][::-1]
    env = New.objects.all().filter(
        ~Q(Type="Breaking"), category="Entertainment & Arts").order_by('-news_id')[:4][::-1]
    new = {"breaking": breaking, "india": india,
           "world": world, "election": election, "business": business, "tech": tech, "science": science, "health": health, "env": env}
    return render(request, "news_app/index.html", new)


def news_about(request, slug):
    news = New.objects.get(slug=slug)
    related = New.objects.all().filter(
        category=news.category).order_by('-news_id')[:5][::-1]
    top = New.objects.all().order_by('-news_id')[:20][::-1]
    news = {"news": news, "related": related, "top": top}
    return render(request, "news_app/news_about.html", news)


def news_category(request, category):
    news1 = New.objects.all().filter(
        category=category).order_by('-news_id')[:4][::-1]
    news2 = New.objects.all().filter(
        category=category).order_by('-news_id')[4:]
    news = {"news1": news1, "news2": news2, "category": category}
    return render(request, 'news_app/category.html', news)


def sport_list(request):
    just = Sport.objects.all().order_by('-sports_id')[:2][::-1]
    breaking = Sport.objects.all().filter(
        Type="Breaking").order_by('-sports_id')[:5][::-1]
    cricket = Sport.objects.all().filter(
        ~Q(Type="Breaking"), category="Cricket").order_by('-sports_id')[:4][::-1]
    football = Sport.objects.all().filter(
        ~Q(Type="Breaking"), category="Football").order_by('-sports_id')[:4][::-1]
    hockey = Sport.objects.all().filter(
        ~Q(Type="Breaking"), category="Hockey").order_by('-sports_id')[:4][::-1]
    kabaddi = Sport.objects.all().filter(
        ~Q(Type="Breaking"), category="Kabaddi").order_by('-sports_id')[:4][::-1]
    basketball = Sport.objects.all().filter(
        ~Q(Type="Breaking"), category="Basketball").order_by('-sports_id')[:4][::-1]
    others = Sport.objects.all().filter(
        ~Q(Type="Breaking"), category="Others").order_by('-sports_id')[:4][::-1]
    sport = {"breaking": breaking, "cricket": cricket, "football": football,
             "hockey": hockey, "kabaddi": kabaddi, "basketball": basketball, "others": others, "just": just}
    return render(request, "news_app/sports_list.html", sport)


def sports_about(request, slug):
    news = Sport.objects.get(slug=slug)
    related = Sport.objects.all().filter(
        category=news.category).order_by('-sports_id')[:5][::-1]
    top = Sport.objects.all().order_by('-sports_id')[:20][::-1]
    news = {"news": news, "related": related, "top": top}
    return render(request, "news_app/sports_about.html", news)


def sports_category(request, category):
    news1 = Sport.objects.all().filter(
        category=category).order_by('-sports_id')[:4][::-1]
    news2 = Sport.objects.all().filter(
        category=category).order_by('-sports_id')[4:]
    news = {"news1": news1, "news2": news2, "category": category}
    return render(request, 'news_app/sports_category.html', news)


def videos(request):
    video = Video.objects.all()
    news = New.objects.all().filter(
        Type="Breaking").order_by('-news_id')[:5][::-1]
    sport = Sport.objects.all().filter(
        Type="Breaking").order_by('-sports_id')[:5][::-1]
    video = {"video": video, "sport": sport, "news": news}
    return render(request, 'news_app/videos.html', video)


def tv(request):
    tv = Tv.objects.all()
    count = tv.count()
    tv = {"tv": tv, "count": count}
    return render(request, 'news_app/tv.html', tv)


def weather(request):
    weather1 = Weather.objects.all().order_by('-weather_id')[:6][::-1]
    weather2 = Weather.objects.all().order_by('-weather_id')[6:]
    weather = {"weather1": weather1, "weather2": weather2}
    return render(request, 'news_app/weather.html', weather)


def weather_about(request, slug):
    weather = Weather.objects.get(slug=slug)
    related = Weather.objects.all().order_by('-weather_id')[:5][::-1]
    top = New.objects.all().order_by('-news_id')[:20][::-1]
    weather = {"weather": weather, "related": related, "top": top}
    return render(request, "news_app/weather_about.html", weather)


def search(request):
    search = request.GET['search']
    if len(search) > 50:
        news = New.objects.none()
        sports = Sport.objects.none()
        weather = Weather.objects.none()
        query = chain(sports, news)
    else:
        sports = Sport.objects.filter(
            description__icontains=search)
        news = New.objects.filter(
            description__icontains=search)
        weather = Weather.objects.filter(
            description__icontains=search)
        query = list(chain(sports, news, weather))
    quer = {"query": query, "search": search}
    return render(request, 'news_app/search.html', quer)


def Contactt(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        mob = request.POST.get('mob', '')
        textarea = request.POST.get('textarea', '')
        if len(name) < 3 or len(textarea) < 10:
            return render(request, "news_app/Contact.html")
        else:
            contact = Contact(name=name, email=email,
                              mob=mob, textarea=textarea)
            contact.save()
    return render(request, "news_app/Contact.html")
