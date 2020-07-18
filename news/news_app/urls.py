from django.urls import path
from . import views
app_name = 'news_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('sports', views.sport_list, name="sport_list"),
    path('search', views.search, name='search'),
    path('category/<str:category>', views.news_category, name='news_category'),
    path('news/<slug>', views.news_about, name='news_about'),
    path('about/<slug>', views.sports_about, name='sports_about'),
    path('weather/<slug>', views.weather_about, name='weather_about'),
    path('sportsCategory/<str:category>',
         views.sports_category, name='sports_category'),
    path('tv', views.tv, name="tv"),
    path('videos', views.videos, name="videos"),
    path('weather', views.weather, name="weather"),
    path('Contact', views.Contactt, name='Contact'),
]
