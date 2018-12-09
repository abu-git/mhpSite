from django.urls import path
from .views import HomePageView, ContactPageView, JourneyPageView, SinglesPageView, TapesPageView, PhotosPageView, VideosPageView

urlpatterns = [
	path('', HomePageView.as_view(), name='mhp-home'),
	path('journey/', JourneyPageView.as_view(), name='mhp-journey'),
	path('tapes/', TapesPageView.as_view(), name='mhp-tapes'),
	path('photos/', PhotosPageView.as_view(), name='mhp-photos'),
	path('videos/', VideosPageView.as_view(), name='mhp-videos'),
	path('singles/', SinglesPageView.as_view(), name='mhp-singles'),
	path('contact/', ContactPageView.as_view(), name='mhp-contact'),

]