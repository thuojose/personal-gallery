from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name='index'),
    url('^today/$',views.today_photos,name='photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_photos,name = 'pastPhotos'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^imagedetails/(\d+)',views.imagedetails,name='imagedetails'),
    url(r'^category/(\d+)',views.category,name='category'),
    url(r'^location/(\d+)',views.location,name='location'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

