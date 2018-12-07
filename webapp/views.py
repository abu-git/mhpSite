from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'home.html'

class JourneyPageView(TemplateView):
	template_name = "journey.html"

class TapesPageView(TemplateView):
	template_name= "mhp-tapes.html"

class PhotosPageView(TemplateView):
	template_name = 'mhp-photos.html'

class VideosPageView(TemplateView):
	template_name = 'mhp-videos.html'

class SinglesPageView(TemplateView):
	template_name = 'mhp-singles.html'



