from django.urls import path
from .views import HomePageView, JourneyPageView, TapesPageView, PhotosPageView, VideosPageView

urlpatterns = [
	path('', HomePageView.as_view(), name='mhp-home'),
	path('journey/', JourneyPageView.as_view(), name='mhp-journey'),
	path('tapes/', TapesPageView.as_view(), name='mhp-tapes'),
	path('photos/', PhotosPageView.as_view(), name='mhp-photos'),
	path('videos/', VideosPageView.as_view(), name='mhp-videos'),
]