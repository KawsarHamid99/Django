from django.shortcuts import render
from django.views.generic import RedirectView,TemplateView
# Create your views here.


class youtubeView(RedirectView):
    url='https://www.facebook.com/'


class GeeckRedirectView(RedirectView):
    #url="/"
    pattern_name='mindex'


