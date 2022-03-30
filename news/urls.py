from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import re_path as url


urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    # url('^today/$',views.news_of_day,name='newsToday'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')
    url(r'^$',views.news_of_day,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^new/article$', views.new_article, name='new-article')
    ]
    
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#    url( r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),
# ]