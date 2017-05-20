"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from article.views import RSSFeed
from article import views   

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home'),  #由于目前只有一个app, 方便起见, 就不设置include了
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^aboutme/$', 'article.views.about_me', name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
    url(r'^search/$','article.views.blog_search', name = 'search'),
#    url(r'^feed/$', RSSFeed(), name = "RSS"),  #新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url
#    url(r'^tinymce/', include('tinymce.urls')),
#    url(r'^sub_comment/$', 'article.views.sub_comment',name='sub_comment'),        #新增sub_comment
    url(r'^comments/', include('django_comments.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')), 
]
